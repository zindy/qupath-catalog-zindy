import requests
import os
from extension_catalog_model.model import *

GITHUB_USER = "zindy"
REPO_PREFIX = "qupath-extension"
QUPATH_VERSION = "v0.7.0"

# Optional: set GITHUB_TOKEN env var to avoid rate limiting
# Get your token here: https://github.com/settings/tokens
HEADERS = {}
token = os.environ.get("GITHUB_TOKEN")
if token:
    HEADERS["Authorization"] = f"Bearer {token}"


def get_qupath_extension_repos(user: str, prefix: str) -> list[dict]:
    """Fetch all public repos for a user that start with the given prefix."""
    repos = []
    page = 1
    while True:
        resp = requests.get(
            f"https://api.github.com/users/{user}/repos",
            headers=HEADERS,
            params={"per_page": 100, "page": page, "type": "public"},
        )
        resp.raise_for_status()
        batch = resp.json()
        if not batch:
            break
        repos.extend(r for r in batch if r["name"].startswith(prefix))
        page += 1
    return repos


def get_latest_release(owner: str, repo: str) -> dict | None:
    """Return the latest release for a repo, or None if there isn't one."""
    resp = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}/releases/latest",
        headers=HEADERS,
    )
    if resp.status_code == 404:
        return None
    resp.raise_for_status()
    return resp.json()


def find_jar_url(release: dict) -> str | None:
    """Pick the first .jar asset from a release."""
    for asset in release.get("assets", []):
        if asset["name"].endswith(".jar"):
            return asset["browser_download_url"]
    return None


def find_optional_deps(release: dict) -> list[str]:
    """
    Pick any non-.jar assets (e.g. .zip dependency bundles).
    Adjust this logic if you use a naming convention for optional deps.
    """
    return [
        asset["browser_download_url"]
        for asset in release.get("assets", [])
        if not asset["name"].endswith(".jar")
    ]


# ── Build the catalog ──────────────────────────────────────────────────────────

repos = get_qupath_extension_repos(GITHUB_USER, REPO_PREFIX)
print(f"Found {len(repos)} repos matching '{REPO_PREFIX}*'\n")

extensions = []

for repo in repos:
    name = repo["name"]
    print(f"Checking {name} …", end=" ")

    release = get_latest_release(GITHUB_USER, name)
    if release is None:
        print("no release, skipping.")
        continue

    tag = release["tag_name"]
    jar_url = find_jar_url(release)
    if jar_url is None:
        print(f"release {tag} found but no .jar asset, skipping.")
        continue

    optional_deps = find_optional_deps(release)
    print(f"✓  {tag}")

    version_range = VersionRange(min=QUPATH_VERSION)

    rel = Release(
        name=tag,
        main_url=jar_url,
        optional_dependency_urls=optional_deps or None,
        version_range=version_range,
    )

    # Use repo metadata for description / homepage; override manually if needed
    ext = Extension(
        name=repo.get("name", name).replace("-", " ").title(),
        description=repo.get("description") or f"QuPath extension: {name}",
        author=GITHUB_USER,
        homepage=repo["html_url"],
        releases=[rel],
    )
    extensions.append(ext)

catalog = Catalog(
    name=f"{GITHUB_USER} QuPath catalog",
    description=f"QuPath extensions by {GITHUB_USER}, targeting QuPath {QUPATH_VERSION}+",
    extensions=extensions,
)

out = "catalog.json"
with open(out, "w") as f:
    f.write(catalog.model_dump_json(indent=2))
    print(f"\n{f.name} written ({len(extensions)} extension(s))")