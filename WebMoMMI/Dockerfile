# Use a base image with Rust
FROM rust:1.33

# Set the working directory in the container
WORKDIR /app

# Install Rust components and set the nightly toolchain as default
RUN rustup toolchain install nightly
RUN rustup default nightly

# Copy the project files into the container
COPY . /app

RUN cargo +nightly build


#EXPOSE 40000
# Command to run the Rust application with the nightly toolchain
CMD ["cargo", "+nightly", "run"]
