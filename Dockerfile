# Use an official Node.js runtime as a parent image
FROM node:18

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and yarn.lock to the working directory
COPY package.json yarn.lock ./

# Install dependencies using Yarn
RUN yarn install

# Copy the rest of the application code to the working directory
COPY . .

# Generate Prisma client
RUN yarn prisma generate

# Expose the port the app runs on
EXPOSE 3000

# Start the NestJS application
CMD ["yarn", "start", "--watch"]