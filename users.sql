CREATE TABLE "users" (
	"user_id"	TEXT NOT NULL,
	"user_email"	TEXT NOT NULL UNIQUE,
	"user_password"	TEXT NOT NULL,
	"created_on"	TEXT NOT NULL,
	PRIMARY KEY("user_id")
);
