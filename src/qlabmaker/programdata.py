

panel = [
"MegClarke",
"ReeseWright",
"StephenHey",
"VivyZhao",
]

# Day 1



speakers1 = {
	"00_StianDavies": ["StianDavies"],
	"01_StuartSumida": ["StuartSumida"],
	"02_PeterRocchio": ["PeterRocchio"],
	"03_Panel": ["Panel", *panel],
	"04_SofiaRomualdo": ["SofiaRomualdo"],
	"05_NainitaDesai": ["NainitaDesai"],
}

skip1 = {
	"00_StianDavies": ['Title', 'Combo', 'Intro'],
	"01_StuartSumida": [],
	"02_PeterRocchio": [],
	"03_Panel": ['Title', 'Intro'],
	"04_SofiaRomualdo": [],
	"05_NainitaDesai": [],

	# hack
	"Panel": ['Name', 'Combo'],
	"Hosts": [],
}


shortnames1 = {
	"Hosts": ["Sylvia", "Satish", "Des"],
	"00_StianDavies": ['Stian'],
	"01_StuartSumida": ['Stuart'],
	"02_PeterRocchio": ['Peter'],
	"03_Panel": ['Panel', 'Meg', 'Reese', 'Stephen', 'Vivy'],
	"04_SofiaRomualdo": ['Sofia'],
	"05_NainitaDesai": ['Nainita'],
}

# Day 2


speakers2 = {
	"01_RayChase": ["RayChase", "Des"],
	"02_HelenKaur": ["HelenKaur"],
	"03_SolBrennan": ["SolBrennan"],
	"04_Martin&Marilena": ["MarilenaPapacosta", "MartinWein", "Martin&Marilena"],
	"05_MikeMcCarthy": ["MikeMcCarthy"]
}

skip2 = {
	"01_RayChase": [],
	"02_HelenKaur": [],
	"03_SolBrennan": [],
	"04_Martin&Marilena": [],
	"05_MikeMcCarthy": [],

	#hack
	"MartinWein": ['Title', 'Intro'],
	"MarilenaPapacosta": ['Title', 'Intro'],
	"Martin&Marilena": ['Name', 'Combo']
}

