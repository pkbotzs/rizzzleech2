FROM powerleech/leechbot:latest

COPY . .

# RUN uv pip install --no-cache \
#         pyrofork

CMD ["bash", "start.sh"]
