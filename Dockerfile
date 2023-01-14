FROM python:3.10

WORKDIR /root/proj

COPY . .

RUN pip3 install --upgrade pip
RUN pip3 install poetry
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi --no-root

EXPOSE 80

CMD streamlit run Home.py
