FROM node:latest

EXPOSE 3000
EXPOSE 35729

WORKDIR /app

# Add /app/node_modules/.bin to environment variables
ENV PATH /app/node_modules/.bin:$PATH

# Copy packages files and install app dependencies
COPY package.json ./package.json
COPY yarn.lock ./yarn.lock
RUN yarn install

# Add React app to working directory
ADD . /app

# Start the React app
CMD ["yarn", "start"]