# Use a lightweight node image as the base image
FROM oven/bun:latest as builder

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and lock files first
COPY package.json bun.lockb /app/

# Install dependencies using bun
RUN bun install

# Copy the rest of the application files
COPY . .

# Build the React app using Vite
RUN bun run build

FROM nginx:alpine

# Remove the default NGINX static assets (optional, for cleanliness)
RUN rm -rf /usr/share/nginx/html/*

# Copy the built React app from the builder stage
COPY --from=builder /app/dist /usr/share/nginx/html

# Copy a custom NGINX config if needed (optional)
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80 to the outside world
EXPOSE 80

# Start NGINX
CMD ["nginx", "-g", "daemon off;"]
