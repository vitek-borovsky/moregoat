# Use the official Node.js image as the base image
FROM node:18-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json (or yarn.lock) to the container
COPY package*.json ./

# Install dependencies (including Tailwind, Vite, React, etc.)
RUN npm install

# Copy the rest of the application files to the container
COPY . .

# For now silencing warnings #TODO
RUN npm run build ||:

EXPOSE 5173

ENTRYPOINT ["npm", "run", "dev"]
