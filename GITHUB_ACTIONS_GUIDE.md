# 🚀 GitHub Actions Build Guide

This guide explains how to use GitHub Actions to automatically build executables for Windows, macOS, and Linux.

## 🎯 What This Does

When you push code to GitHub, it will **automatically**:
- ✅ Build `.exe` for Windows
- ✅ Build `.app` for macOS  
- ✅ Build executable for Linux
- ✅ Make them available for download as artifacts

**No Mac or Linux computer needed!** GitHub does all the building for you.

## 📋 Setup Steps

### 1. Create a GitHub Repository

If you haven't already:

```bash
# Initialize git in your project folder
cd M:\Courses\CODE\CLT
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit with GitHub Actions"

# Create repo on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

### 2. Verify GitHub Actions is Running

1. Go to your repository on GitHub
2. Click the **"Actions"** tab
3. You should see a workflow running called "Build Executables"
4. Wait for it to complete (usually 5-10 minutes)

### 3. Download Your Executables

Once the workflow completes:

1. Go to the **Actions** tab
2. Click on the latest workflow run
3. Scroll down to **"Artifacts"**
4. Download:
   - `SlideAudioGenerator-Windows` (contains .exe)
   - `SlideAudioGenerator-macOS` (contains .app)
   - `SlideAudioGenerator-Linux` (contains executable)

## 🎬 Manual Trigger

You can also trigger builds manually:

1. Go to **Actions** tab
2. Click **"Build Executables"** workflow
3. Click **"Run workflow"** button
4. Select branch and click **"Run workflow"**

## 🏷️ Creating Releases

To create a public release with downloads:

```bash
# Tag your version
git tag v1.0.0
git push origin v1.0.0
```

This will:
- Trigger the build workflow
- Create a GitHub Release
- Automatically attach all executables to the release

Users can then download from the **Releases** page.

## 📊 Build Status Badge

Add this to your README.md to show build status:

```markdown
![Build Status](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/workflows/Build%20Executables/badge.svg)
```

## 🔧 Troubleshooting

### Build fails on a specific OS

Check the workflow logs:
1. Go to Actions tab
2. Click the failed workflow
3. Click on the failed job (Windows/macOS/Linux)
4. Review the logs

### "Module not found" errors

Make sure all dependencies are in `requirements.txt`:
```bash
pip freeze > requirements.txt
```
Then commit and push.

### Artifacts not appearing

- Artifacts are only created if the build succeeds
- Check the workflow logs for errors
- Artifacts expire after 90 days by default

## 💰 Cost

GitHub Actions is **FREE** for public repositories with generous limits:
- 2,000 minutes/month for private repos
- Unlimited for public repos

## 🎨 Customization

### Change when builds run

Edit `.github/workflows/build-executables.yml`:

```yaml
on:
  push:
    branches: [ main ]  # Only on main branch
  # Remove 'pull_request' if you don't want builds on PRs
```

### Change Python version

```yaml
- name: Set up Python
  uses: actions/setup-python@v5
  with:
    python-version: '3.11'  # Change this
```

### Skip Linux builds

Remove the `ubuntu-latest` entry from the matrix in the workflow file.

## 📚 Next Steps

1. **Test locally first**: Run `python build_cross_platform.py` to test
2. **Push to GitHub**: Let Actions build for all platforms
3. **Create releases**: Tag versions for public downloads
4. **Share links**: Direct users to the Releases page

## 🔗 Useful Links

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [PyInstaller Documentation](https://pyinstaller.org/)
- [GitHub Releases Guide](https://docs.github.com/en/repositories/releasing-projects-on-github)

---

**Questions?** Check the workflow logs or open an issue in your repository.
