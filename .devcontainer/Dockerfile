FROM debian:stable-slim
ENV TZ=America/Bogota

# Install uv and uvx
COPY --from=ghcr.io/astral-sh/uv:0.8.14 /uv /uvx /bin/

# Install dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    wget \
    vim \
    fish \
    make \
    unzip \
    sshpass \
    ca-certificates \
    python3 \
    python3-pip

# Install Node.js 22.x
# RUN curl -fsSL https://deb.nodesource.com/setup_22.x | sh - \
#     && apt-get install -y nodejs chromium

# Clean up
RUN apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/* 
# Add non-root user
RUN groupadd -g 1000 audeldiaz \
    && useradd -u 1000 -g 1000 -ms /usr/bin/fish audeldiaz \
    && chown -R audeldiaz:audeldiaz /home/audeldiaz

USER audeldiaz

CMD [ "/usr/bin/fish" ]