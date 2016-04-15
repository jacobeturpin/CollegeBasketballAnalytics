CREATE TABLE Player (
	Id			varchar(36)			NOT NULL,
	Name		varchar(250)		NOT NULL,
	Link		nvarchar(max)		NOT NULL
);


CREATE TABLE Team (
	Id			varchar(36)			NOT NULL,
	Name		varchar(250)		NOT NULL,
	Link		nvarchar(max)		NOT NULL
);


CREATE TABLE Game (
	Id				varchar(36)			NOT NULL,
	"Date"			datetime			NOT NULL,
	Link			nvarchar(max)		NOT NULL,
	"Type"			integer				NOT NULL,
	IsNeturalSite	bit					NOT NULL,
	HomeTeamId		varchar(36)			NOT NULL,
	HomeTeamScore	integer				NOT NULL,
	AwayTeamId		varchar(36)			NOT NULL,
	AwayTeamScore	integer				NOT NULL
);

/*
CREATE TABLE PlayerBoxScore (
	PlayerId	varchar(36)		NOT NULL,
	GameId		varchar(36)		NOT NULL,
	MP			integer			NOT NULL,
	FGM			integer			NULL,
	FGA			integer			NULL,
	FGP			decimal			NULL,
) */
