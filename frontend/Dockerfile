# Step 1: Build the Vue.js app
FROM node:latest AS build-stage

WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy source code
COPY . .

# Build the project
RUN npm run build

# Step 2: Serve with Nginx
FROM nginx:stable-alpine AS production-stage

# Copy the built app from the previous stage
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Copy custom nginx config (optional)
# Make sure you have nginx.conf in your project root
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
