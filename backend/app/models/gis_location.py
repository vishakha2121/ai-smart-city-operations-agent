git add .cd C:\Users\YourName\ai-smart-city-operations-agent

# Create files
notepad README.md
notepad .gitignore
notepad LICENSE

# Initialize
git init

# Add all (except ignored)
git add .

# Verify what's being added
git status

# Commit
git commit -m "Initial commit: AI Smart City Operations Agent with README, LICENSE, .gitignore"

# Push
git branch -M main
git remote add origin https://github.com/vishakha2121/ai-smart-city-operations-agent.git
git push -u origin main