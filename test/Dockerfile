FROM alpine

RUN	apk update && \
	apk upgrade && \
	apk add --update openssl nginx && \
	mkdir /etc/nginx/certificates && \
	openssl req \
		-x509 \
		-newkey rsa:2048 \
		-keyout /etc/nginx/certificates/key.pem \
		-out /etc/nginx/certificates/cert.pem \
		-days 365 \
		-nodes \
		-subj /CN=localhost && \
	mkdir /www && \
  mkdir -p /run/nginx && \
	rm -rf /var/cache/apk/*

COPY nginx.conf /etc/nginx/nginx.conf
COPY html www/ 
COPY html/* /usr/share/nginx/html/

# Expose volumes
VOLUME ["/etc/nginx/conf.d", "/var/log/nginx", "/www"]

# Expose ports
EXPOSE 80 443

# Entry point
ENTRYPOINT ["/usr/sbin/nginx", "-g", "daemon off;"]