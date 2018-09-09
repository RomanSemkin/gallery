upstream gallery {
    server gallery:9000;
}
server {
    listen 80;

    location / {
        access_log /var/artuser/logs/nginx_gallery_access.log;
        error_log /var/artuser/logs/nginx_gallery_error.log;
        client_max_body_size 30M;
        include uwsgi_params;
        uwsgi_pass gallery;
    }
    location /media {
        access_log off;
        alias /home/artuser/dist/static_cdn/media_root;
    }
    location /static {
        access_log off;
        alias /home/artuser/dist/static_project;
    }
}
/usr/local/var/log/nginx/

server {
        listen 80;
        #server_name localhost; # substitute your machine's IP address or FQDN
        charset utf-8;

        # max upload size
        client_max_body_size 75M;

        location /media  {
           alias /Users/boogaloosurf/PycharmProjects/Gallery_django_2/src/static_cdn/media_root;  # your Django project's media files - amend as required
       }
         location /static {
           alias /Users/boogaloosurf/PycharmProjects/Gallery_django_2/src/static_project; # your Django project's static files - amend as required
       }
        location / {
            unix:/Users/boogaloosurf/PycharmProjects/Gallery_django_2/src/gallery/uwsgi.sock;
           include /Users/boogaloosurf/PycharmProjects/Gallery_django_2/src/uwsgi_params;
        }
}

server {
    listen 80;
    charset utf-8;
    client_max_body_size 30M;
    keepalive_timeout  0;
    sendfile        on;

    location / {
        access_log /var/artuser/logs/nginx_gallery_access.log;
        error_log /var/artuser/logs/nginx_gallery_error.log;
        include uwsgi_params;
        uwsgi_pass gallery_django_2_gallery_1:9000;
    }
    location /media {
        access_log off;
        alias /home/artuser/dist/static_cdn/media_root;
    }
    location /static {
        access_log off;
        alias /home/artuser/dist/static_project;
    }
}