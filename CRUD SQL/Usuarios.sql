USE [INDUSTRIA_WAYNE]
GO

/****** Object:  Table [dbo].[Usuarios]    Script Date: 17/11/2024 21:54:17 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Usuarios](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[username] [varchar](50) NOT NULL,
	[senha_hash] [varchar](255) NOT NULL,
	[nome_completo] [varchar](100) NULL,
	[email] [varchar](100) NULL,
	[role] [varchar](20) NULL,
	[data_criacao] [datetime] NULL,
	[data_ultima_login] [datetime] NULL,
	[ativo] [bit] NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
UNIQUE NONCLUSTERED 
(
	[email] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
UNIQUE NONCLUSTERED 
(
	[username] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[Usuarios] ADD  DEFAULT (getdate()) FOR [data_criacao]
GO

ALTER TABLE [dbo].[Usuarios] ADD  DEFAULT ((1)) FOR [ativo]
GO

ALTER TABLE [dbo].[Usuarios]  WITH CHECK ADD CHECK  (([role]='admin' OR [role]='gerente' OR [role]='funcionario'))
GO


