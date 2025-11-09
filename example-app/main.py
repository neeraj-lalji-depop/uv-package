"""Example app that uses my-package-neerajlalji in editable mode"""

from my_package_neerajlalji import hello
import httpx


def main():
    # Use your package (in editable mode!)
    message = hello()
    print(f"Package says: {message}")

    # Use this app's own dependencies
    print("\n--- Testing httpx (this app's dependency) ---")
    response = httpx.get("https://api.github.com/zen")
    print(f"GitHub Zen: {response.text}")

    print("\n✅ This app has its own dependencies (httpx)")
    print("✅ Your package is installed in EDITABLE mode")
    print("✅ Changes to my-package-neerajlalji will reflect immediately!")


if __name__ == "__main__":
    main()
