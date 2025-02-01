# Use an official Node.js runtime as the base image
FROM node:18-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the frontend code
COPY . .

# Build the React app for production
RUN npm run build

# Install a lightweight HTTP server to serve the frontend
RUN npm install -g serve

# Expose the port the frontend runs on
EXPOSE 3000

# Command to serve the frontend
CMD ["serve", "-s", "build", "-l", "3000"]