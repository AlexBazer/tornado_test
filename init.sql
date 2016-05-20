USE imonomy_db;
TRUNCATE TABLE imonomy_data;
TRUNCATE TABLE networks;
TRUNCATE TABLE publishers;
TRUNCATE TABLE websites;

INSERT into networks (name) values ('net_1');
INSERT into networks (name) values ('net_2');
INSERT into networks (name) values ('net_3');
INSERT into networks (name) values ('net_4');

INSERT into publishers (name) values ('pub_1');
INSERT into publishers (name) values ('pub_2');
INSERT into publishers (name) values ('pub_3');
INSERT into publishers (name) values ('pub_4');

INSERT into websites (name) values ('web_1');
INSERT into websites (name) values ('web_2');
INSERT into websites (name) values ('web_3');
INSERT into websites (name) values ('web_4');

INSERT into imonomy_data (network_id, publisher_id, website_id, domains, os_name, device_name) values (1,1,1, "dom1, dom2", "linix", "desktop");
INSERT into imonomy_data (network_id, publisher_id, website_id, domains, os_name, device_name) values (1,2,1, "dom2, dom3", "windows", "mobile");
INSERT into imonomy_data (network_id, publisher_id, website_id, domains, os_name, device_name) values (1,2,2, "dom3, dom4", "ios", "desktop");
INSERT into imonomy_data (network_id, publisher_id, website_id, domains, os_name, device_name) values (1,3,2, "dom4, dom5", "windows", "mobile");
INSERT into imonomy_data (network_id, publisher_id, website_id, domains, os_name, device_name) values (1,3,3, "dom4, dom5", "ios", "desktop");
INSERT into imonomy_data (network_id, publisher_id, website_id, domains, os_name, device_name) values (2,1,1, "dom1, dom2", "linix", "mobile");
INSERT into imonomy_data (network_id, publisher_id, website_id, domains, os_name, device_name) values (2,2,1, "dom2, dom3", "windows", "desktop");
INSERT into imonomy_data (network_id, publisher_id, website_id, domains, os_name, device_name) values (2,2,2, "dom3, dom4", "ios", "mobile");
INSERT into imonomy_data (network_id, publisher_id, website_id, domains, os_name, device_name) values (2,3,2, "dom4, dom5", "windows", "desktop");
INSERT into imonomy_data (network_id, publisher_id, website_id, domains, os_name, device_name) values (2,3,3, "dom4, dom5", "linix", "mobile");
INSERT into imonomy_data (network_id, publisher_id, website_id, domains, os_name, device_name) values (3,1,1, "dom1, dom2", "windows", "desktop");
INSERT into imonomy_data (network_id, publisher_id, website_id, domains, os_name, device_name) values (3,2,1, "dom2, dom3", "ios", "mobile");
INSERT into imonomy_data (network_id, publisher_id, website_id, domains, os_name, device_name) values (3,2,2, "dom3, dom4", "windows", "desktop");
INSERT into imonomy_data (network_id, publisher_id, website_id, domains, os_name, device_name) values (3,3,2, "dom4, dom5", "linix", "desktop");
INSERT into imonomy_data (network_id, publisher_id, website_id, domains, os_name, device_name) values (3,3,3, "dom4, dom5", "ios", "tablet");
