# Upload this project to GitHub

The repository in this archive is **prepared locally**; it has not yet been created on your GitHub account.

## Option A — GitHub website (easiest)

1. Sign in at https://github.com/ and open https://github.com/new.
2. Set the **Repository name** to `weekly-mortality-forecasting` (or a different name you prefer).
3. Choose **Private** initially so you can review author contact information, notebooks and data licensing. You may change it to Public once you decide it is safe and the course requires public access.
4. Do **not** select *Add a README*, *.gitignore* or a license: this package already contains README and .gitignore and deliberately does not assign a software license.
5. Create the empty repository.
6. On its *Quick setup* page, use **uploading an existing file**, drag in the *contents* of this unzipped folder, and commit. For deeply nested folders or many files, a local Git push is more reliable.
7. Confirm that `README.md`, all **6 notebooks**, `requirements.txt`, the **5 data/reference files**, `report/`, `slides/`, and `dashboard/` appear on GitHub.
8. Copy the confirmed repo URL into your course GitHub/Drive link folder and LMS submission.

## Option B — Git (best for full folders)

From the extracted project folder:

```bash
git init
git branch -M main
git add .
git commit -m "Add reproducible mortality forecasting project"
git remote add origin https://github.com/YOUR_USERNAME/weekly-mortality-forecasting.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username and create the empty repository first. Authenticate when prompted (GitHub password alone is not a supported command-line authentication method; use Git Credential Manager, GitHub CLI or a token as appropriate).

## Before making it Public

- Review `report/*.pdf`, `slides/*.pptx` and notebook outputs for names, university details and email addresses.
- Never commit passwords, `.env` files, authentication tokens or an unredacted personal AI Audit Log.
- Respect the source attributions and applicable ONS/Met Office reuse terms.
- Run `python scripts/verify_data.py` and, ideally, the Jupyter `Restart & Run All Cells` check on your own machine.

## Teacher access

For a **Public** repository, your teacher can open the repository URL. For a **Private** repository, you must grant the required repository access through GitHub before sharing the URL; a private URL alone will not grant access.
