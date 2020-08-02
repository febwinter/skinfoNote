FROM mysql:5.7.31
COPY autodump.sh /autodump.sh
COPY create_table.sql /create_table.sql
RUN cp -r /var/lib/mysql /var/lib/mysql-no-volume
CMD ["--datadir", "/var/lib/mysql-no-volume"]