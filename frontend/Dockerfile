# Stage 1: Build React app
FROM node:latest as build

EXPOSE 3000
EXPOSE 35729

WORKDIR /app

# Add /app/node_modules/.bin to environment variables
ENV PATH /app/node_modules/.bin:$PATH

# Copy packages files and install app dependencies
COPY package.json ./package.json
COPY yarn.lock ./yarn.lock
RUN yarn install

# Add source to working directory
COPY . /app

# Start the React app
RUN yarn build

# Stage 2: Serve using NGINX
FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]