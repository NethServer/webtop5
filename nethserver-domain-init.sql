INSERT INTO "core"."domains" ("domain_id", "internet_name", "enabled", "description", "user_auto_creation", "dir_uri", "dir_admin", "dir_password", "dir_connection_security", "dir_case_sensitive", "dir_password_policy", "dir_parameters") VALUES ('NethServer', 'nethesis.lan', 't', 'NethServer', 't', 'ldapneth://localhost:389', 'cn=ldapservice,dc=directory,dc=nh', 'OMeHWrBQgmANbvmxqs17uHA8j2EsKfSm', NULL, 'f', 'f', '{"loginDn":"ou=People,dc=directory,dc=nh","loginFilter":null,"userDn":"ou=People,dc=directory,dc=nh","userFilter":null,"userFirstnameField":"givenName","userLastnameField":"sn","userDisplayNameField":"gecos"}');



INSERT INTO "core"."users" ("domain_id", "user_id", "type", "enabled", "user_uid", "display_name", "secret") VALUES ('NethServer', 'admins', 'G', 't', '4383a654-633e-4fb6-bf8d-7f197d9c8148', 'Admins', NULL);
INSERT INTO "core"."users" ("domain_id", "user_id", "type", "enabled", "user_uid", "display_name", "secret") VALUES ('NethServer', 'users', 'G', 't', '0f4d4fa7-7f21-48c0-96c9-fc6d861cc8fe', 'Users', NULL);



INSERT INTO "core"."roles_permissions" ("role_uid", "service_id", "key", "action", "instance") VALUES ('0f4d4fa7-7f21-48c0-96c9-fc6d861cc8fe', 'com.sonicle.webtop.core', 'SERVICE', 'ACCESS', 'com.sonicle.webtop.calendar');
INSERT INTO "core"."roles_permissions" ("role_uid", "service_id", "key", "action", "instance") VALUES ('0f4d4fa7-7f21-48c0-96c9-fc6d861cc8fe', 'com.sonicle.webtop.core', 'SERVICE', 'ACCESS', 'com.sonicle.webtop.contacts');
INSERT INTO "core"."roles_permissions" ("role_uid", "service_id", "key", "action", "instance") VALUES ('0f4d4fa7-7f21-48c0-96c9-fc6d861cc8fe', 'com.sonicle.webtop.core', 'SERVICE', 'ACCESS', 'com.sonicle.webtop.mail');
INSERT INTO "core"."roles_permissions" ("role_uid", "service_id", "key", "action", "instance") VALUES ('0f4d4fa7-7f21-48c0-96c9-fc6d861cc8fe', 'com.sonicle.webtop.core', 'SERVICE', 'ACCESS', 'com.sonicle.webtop.tasks');
INSERT INTO "core"."roles_permissions" ("role_uid", "service_id", "key", "action", "instance") VALUES ('0f4d4fa7-7f21-48c0-96c9-fc6d861cc8fe', 'com.sonicle.webtop.core', 'SERVICE', 'ACCESS', 'com.sonicle.webtop.vfs');



//Insert per i permessi di default:
INSERT INTO "core"."roles_permissions" ("role_uid", "service_id", "key", "action", "instance") VALUES ('0f4d4fa7-7f21-48c0-96c9-fc6d861cc8fe', 'com.sonicle.webtop.core', 'DEVICES_SYNC', 'ACCESS', '*');
INSERT INTO "core"."roles_permissions" ("role_uid", "service_id", "key", "action", "instance") VALUES ('0f4d4fa7-7f21-48c0-96c9-fc6d861cc8fe', 'com.sonicle.webtop.core', 'USER_PROFILE_INFO', 'MANAGE', '*');
INSERT INTO "core"."roles_permissions" ("role_uid", "service_id", "key", "action", "instance") VALUES ('0f4d4fa7-7f21-48c0-96c9-fc6d861cc8fe', 'com.sonicle.webtop.mail', 'ACCOUNT_SETTINGS', 'CHANGE', '*');
INSERT INTO "core"."roles_permissions" ("role_uid", "service_id", "key", "action", "instance") VALUES ('0f4d4fa7-7f21-48c0-96c9-fc6d861cc8fe', 'com.sonicle.webtop.mail', 'MAILCARD_SETTINGS', 'CHANGE', '*');

//Insert per impostare i default per la sincronizzazione di categorie/calendari:
//i valori supportati sono 'O' (disattiva), 'R' (sola lettura) e 'W' (lettura/scrittura)
INSERT INTO "core"."settings" ("service_id", "key", "value") VALUES ('com.sonicle.webtop.calendar', 'default.calendar.sync', 'W');
INSERT INTO "core"."settings" ("service_id", "key", "value") VALUES ('com.sonicle.webtop.contacts', 'default.category.sync', 'W');
INSERT INTO "core"."settings" ("service_id", "key", "value") VALUES ('com.sonicle.webtop.tasks', 'default.category.sync', 'W');


//Insert per controllare le info (server/webapp) sulla pagina di login:
INSERT INTO "core"."settings" ("service_id", "key", "value") VALUES ('com.sonicle.webtop.core', 'login.systeminfo.hide', 'true');
INSERT INTO "core"."settings" ("service_id", "key", "value") VALUES ('com.sonicle.webtop.core', 'login.webappname.hide', 'true');

//Insert per impostare la URL di download del Notifier:
INSERT INTO "core"."settings" ("service_id", "key", "value") VALUES ('com.sonicle.webtop.core', 'addon.notifier.url', 'http://...');
