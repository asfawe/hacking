FROM python:3.11-alpine

ENV USER chall
ENV PORT 8000

# Add user
RUN adduser -D -g "" $USER

# Add files
COPY --chown=root:root app /app
COPY --chown=root:$USER flag /flag

WORKDIR /app
RUN chmod 705 run.sh
RUN pip install -r requirements.txt

USER $USER

ENTRYPOINT ["/bin/ash"]
CMD ["./run.sh"]
