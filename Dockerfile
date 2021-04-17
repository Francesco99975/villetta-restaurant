FROM python:3.9-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN \
 apk add --no-cache python3 py3-setuptools \
    tiff-dev jpeg-dev openjpeg-dev zlib-dev freetype-dev lcms2-dev \
    libwebp-dev tcl-dev tk-dev harfbuzz-dev fribidi-dev libimagequant-dev \
    libxcb-dev libpng-dev \
    libjpeg zlib openjpeg postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
    python3 -m pip install -r requirements.txt --no-cache-dir && \
    apk --purge del .build-deps

COPY . .

RUN sed -i 's/assignment_tag/simple_tag/g' /usr/local/lib/python3.9/site-packages/carton/templatetags/carton_tags.py

RUN mv ./villetta/.env_prod ./villetta/.env

EXPOSE 8000

RUN chmod +x entry_point.sh

CMD ["./entry_point.sh"]