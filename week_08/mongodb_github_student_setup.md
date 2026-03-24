# MongoDB Atlas + GitHub Student Setup

## Verified offer
Verified on **March 19, 2026** against GitHub Education and MongoDB Atlas documentation:
- GitHub Student lists a MongoDB offer with **$50 in Atlas credits**
- the offer also includes **MongoDB Compass**
- the offer also includes **MongoDB University access plus a certification benefit**

Official links:
- GitHub Education Pack: https://education.github.com/pack
- MongoDB Atlas free cluster docs: https://www.mongodb.com/docs/atlas/tutorial/deploy-free-tier-cluster/

## Step 1: Make sure GitHub Student is active
1. Go to the GitHub Education Pack page.
2. Sign in with your GitHub account.
3. Confirm that your Student Developer Pack is approved.

## Step 2: Redeem the MongoDB offer
1. On the GitHub Education Pack page, find **MongoDB**.
2. Open the MongoDB offer and follow the redeem flow.
3. Create a MongoDB account or sign in to an existing account.

## Step 3: Create an Atlas project and free cluster
MongoDB Atlas documentation says:
- `M0` clusters are free forever
- Atlas allows one free cluster per project

To create the cluster:
1. In Atlas, create a new project.
2. Click **Create** to create a cluster.
3. Choose the `M0` free option.
4. Pick a provider: AWS, GCP, or Azure.
5. Pick a region close to you.
6. Name the cluster and click **Create**.

## Step 4: Secure the cluster before using it
1. Create a database user with a strong password.
2. Add your current IP address to the Atlas IP access list.
3. Save your username and password somewhere safe.
4. Do not put passwords into GitHub repos or shared class screenshots.

## Step 5: Connect with Compass
1. Install MongoDB Compass if you do not already have it.
2. In Atlas, click **Connect** on your cluster.
3. Copy the Compass connection string.
4. Replace the username and password placeholders.
5. Open Compass and test the connection.

## Security reminders for class
- Prefer your current IP instead of opening access to everyone.
- If you temporarily use a broad IP rule for a demo, remove it after class.
- Use a separate database user for each app or project when possible.
- Think about what data should and should not go into a cloud database.

## Practical note
Even if the Atlas credit redemption takes time, students can still begin with an `M0` free cluster while waiting.
That keeps setup aligned with class even if the promotional benefit is delayed.
