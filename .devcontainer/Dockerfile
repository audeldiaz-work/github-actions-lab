FROM python:3.13-slim
ENV TZ=America/Bogota
ENV PATH="/home/audeldiaz/.venv/bin:${PATH}"

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    wget \
    vim \
    fish \
    make \
    && rm -rf /var/lib/apt/lists/*

RUN python -m venv /home/audeldiaz/.venv \
    && /home/audeldiaz/.venv/bin/pip install --upgrade pip \   
    && /home/audeldiaz/.venv/bin/pip install pytest pytest-cov black pyrefly coverage

RUN groupadd -g 1000 audeldiaz \
    && useradd -u 1000 -g 1000 -ms /usr/bin/fish audeldiaz \
    && chown -R audeldiaz:audeldiaz /home/audeldiaz
    
USER audeldiaz

CMD [ "/usr/bin/fish" ]