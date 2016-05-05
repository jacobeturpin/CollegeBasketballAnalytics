CREATE TABLE Player (
	PlayerId	varchar(36)			PRIMARY KEY,
	Name		varchar(250)		NOT NULL,
	Link		nvarchar(max)		NOT NULL
);

CREATE TABLE Team (
	TeamId		varchar(36)			PRIMARY KEY,
	Name		varchar(250)		NOT NULL,
	Link		nvarchar(max)		NOT NULL
);

CREATE TABLE Game (
	GameId			varchar(36)			PRIMARY KEY,
	GameDate		datetime			NOT NULL,
	Link			nvarchar(max)		NOT NULL,
	GameType		integer				NOT NULL,
	IsNeturalSite	bit					NOT NULL,
	HomeTeamId		varchar(36)			NOT NULL,
	HomeTeamScore	integer				NOT NULL,
	AwayTeamId		varchar(36)			NOT NULL,
	AwayTeamScore	integer				NOT NULL
);

CREATE TABLE PlayerBoxScore (
	BoxScoreId	varchar(36)		PRIMARY KEY,
	PlayerId	varchar(36)		NOT NULL,
	TeamId		varchar(36)		NOT NULL,
	GameId		varchar(36)		NOT NULL,
	MP			integer			NOT NULL,
	FGM			integer			NOT NULL,
	FGA			integer			NOT NULL,
	FGP			decimal			NULL,
	TwoPM		integer			NOT NULL,
	TwoPA		integer			NOT NULL,
	TwoPP		decimal			NULL,
	ThreePM		integer			NOT NULL,
	ThreePA		integer			NOT NULL,
	ThreePP		decimal			NULL,
	FTM			integer			NOT NULL,
	FTA			integer			NOT NULL,
	FTP			decimal			NULL,
	ORB			integer			NOT NULL,
	DRB			integer			NOT NULL,
	TRB			integer			NOT NULL,
	AST			integer			NOT NULL,
	STL			integer			NOT NULL,
	BLK			integer			NOT NULL,
	TOV			integer			NOT NULL,
	PF			integer			NOT NULL,
	PTS			integer			NOT NULL
)

CREATE TABLE TeamBoxScore (
	BoxScoreId	varchar(36)		PRIMARY KEY,
	TeamId		varchar(36)		NOT NULL,
	GameId		varchar(36)		NOT NULL,
	MP			integer			NOT NULL,
	FGM			integer			NOT NULL,
	FGA			integer			NOT NULL,
	FGP			decimal			NULL,
	TwoPM		integer			NOT NULL,
	TwoPA		integer			NOT NULL,
	TwoPP		decimal			NULL,
	ThreePM		integer			NOT NULL,
	ThreePA		integer			NOT NULL,
	ThreePP		decimal			NULL,
	FTM			integer			NOT NULL,
	FTA			integer			NOT NULL,
	FTP			decimal			NULL,
	ORB			integer			NOT NULL,
	DRB			integer			NOT NULL,
	TRB			integer			NOT NULL,
	AST			integer			NOT NULL,
	STL			integer			NOT NULL,
	BLK			integer			NOT NULL,
	TOV			integer			NOT NULL,
	PF			integer			NOT NULL,
	PTS			integer			NOT NULL
)

CREATE TABLE Season(
	Season			varchar(10)		NOT NULL,
	StartDate		date			NOT NULL,
	EndDate			date			NOT NULL,
)

CREATE TABLE GameType(
	GameType		integer			NOT NULL,
	Name			varchar(50)		NOT NULL
)