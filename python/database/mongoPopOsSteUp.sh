#!/usr/bin/env bash


echo "Adding MongoDB to System Software repos..."
sudo apt -q update

echo "Installing GnuPrivacyGaurd(gnupg)..."
sudo apt -q install
echo "GPG installed ..."

echo "Importing MonogoDB GPG key... "
curl -fsSL https://www.mongodb.org/static/pgp/server-8.0.asc | \
sudo gpg -o /usr/share/keyrings/mongodb-server-8.0.gpg \
--dearmor
echo "Imported"

echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-8.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/8.0 multiverse"
echo "Added to system repo..."

echo "Install MongoDB"
sudo apt -q install update
sudo apt -q install mongodb-org -y
echo "MongoDB Successfully installed!"
