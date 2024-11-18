USE [INDUSTRIA_WAYNE]
GO

/****** Object:  Table [dbo].[items_batcaverna]    Script Date: 17/11/2024 21:53:45 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[items_batcaverna](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[nome] [nvarchar](255) NOT NULL,
	[tipo] [nvarchar](50) NOT NULL,
	[quantidade] [int] NOT NULL,
	[descricao] [nvarchar](max) NULL,
	[imagem] [nvarchar](255) NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO


