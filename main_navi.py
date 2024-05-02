"""********************************************************************************  
   Author Information:
   Victor Vu (vuvictor@csu.fullerton.edu)

   Other Authors: 

   Program Information:
   This File: main_navi.py
   Description: Manager for the SmartNavi GPS system. Calls BFS, DFS and Dijkstra's 
   Algorithm for pathfinding. Also incorporates GUI, utilizing a graph model.
********************************************************************************"""  
import gui  # Call the GUI file

# Main function for execution


def main():
    # Paths and Nodes
    adjacency_list = {

    "Art 01": {"StateArt": 1, }
    "Corporate Drive 01": {"State 02": 1, "Corporation Yard": 1,},
    "GymWest": {"WestCamp": 1, "Titan Sport Complex": 3, "Ruby Gerontology Center": 6},
    "Gym Drive 01": {"GymWest": 1, "State College Parking": 1, "Corporation Yard": 1},
    "GymState" : {"Gym Drive 01": 1, "State 02": 1},
    "State 01": {"Parking A": 1},
    "State 02": {"State 01": 1, "Corporate Drive 01": 1, "State 03": 1,},
    "State 03": {"Golleher Alumni House": 1, "State 02": 1, "State 04": 1,},
    "State 04": {"State 03": 1, "Titan Student Union": 2, "StateArt":2},
    "StateArt": {"State 04": 2,},
    "StateNut": {"StateArt": 1,},
    "WestCamp": {"Corporate Drive 01": 1, "Titan Sport Complex": 3,},
    "Yorba 00" : {"Yorba 01": 1,},
    "Yorba 01" : {"Parking G": 1,},
    "Yorba 02" : {"Parking A": 2, "Yorba 01" :1,},



    # to edit with testing
        "Arboretum": {"Housing Office": 3, "Residence Halls": 2, "Titan Sport Complex": 4, "Ruby Gerontology Center": 6, "Titan House": 2},
        "A-South Parking": {"Parking A": 7, "Children's Center": 2, "Parking & Transportation Office": 1, "Corporate Drive 01": 1},
        "Becker Amphitheater": {"Parking E": 4, "Commons": 1},
        "Carl's Jr": {"University Hall": 8, "Langsdorf Hall": 4},
        "Commons": {"Becker Amphitheater": 1, "Pollak Library": 3},
        "Children's Center": {"A-South Parking": 1, "Parking A": 2},
        "Clayes Performing Arts Center": {"Visual Arts": 2, "Quad": 3},
        "Corporation Yard": {"Corporate Drive 01": 1,},
        "Dan Black Hall": {"Langsdorf Hall": 3, "Nutwood Parking": 2},
        "Eastside Parking": {"Parking F": 4, "Greenhouse Complex": 6},
        "Education Classroom": {"Pollak Library": 2, "Parking I": 1},
        "Engineering/ Computer Science": {"Student Heath/ Counseling Center": 6, "Titan Student Union": 8},
        "Golleher Alumni House": {"University Police": 1, "Titan Student Union": 1, "State College Parking":1,},
        "Greenhouse Complex": {"Eastside Parking": 6, "McCarthy Hall": 7},
        "Housing Office": {"Arboretum": 3, "Residence Halls": 2, "Ruby Gerontology Center": 6},
        "Humanities/ Social Sciences": {"Quad": 2, "Parking F": 3},
        "Kinesiology/ Health Science": {"Student Rec Center": 4, "Student Heath/ Counseling Center": 5},
        "Langsdorf Hall": {"Carl's Jr": 4, "Dan Black Hall": 3},
        "McCarthy Hall": {"Greenhouse Complex": 7, "University Hall": 2},
        "Mihaylo Hall": {"Nutwood Parking": 5, "Parking C": 4},
        "Nutwood Parking": {"Dan Black Hall": 2, "Mihaylo Hall": 5},
        "Parking A": {"A-South Parking": 1.5, "Parking & Transportation Office": 1.5, "Children's Center": 1.25},
        "Parking C": {"Mihaylo Hall": 4},
        "Parking E": {},
        "Parking F": {"Humanities/ Social Sciences": 3, "Eastside Parking": 4},
        "Parking G": {},
        "Parking I": {"Education Classroom": 1, "Visual Arts": 5},
        "Parking & Transportation Office": {"Parking A": 2},
        "Pollak Library": {"Commons": 3, "Education Classroom": 2},
        "Quad": {"Clayes Performing Arts Center": 3, "Humanities/ Social Sciences": 2},
        "Residence Halls": {"Arboretum": 2, "Housing Office": 2, "Ruby Gerontology Center": 7},
        "Ruby Gerontology Center": {"Arboretum": 6, "Housing Office": 6, "Residence Halls": 7, "Titan Sport Complex": 5, },
        "State College Parking": {"University Police": 1,   "Student Rec Center": 1, "Golleher Alumni House":1, },
        "Student Heath/ Counseling Center": {"Kinesiology/ Health Science": 5, "Engineering/ Computer Science": 6},
        "Student Housing": {},
        "Student Rec Center": { "Kinesiology/ Health Science": 1, "State College Parking": 1, "Titan Student Union": 1.5,},
        "Titan House": { "Arboretum": 2},
        "Titan Sport Complex": {"Parking A": 3, "Arboretum": 4},
        "Titan Student Union": { "Golleher Alumni House": 1, "State College Parking": 1.5, "Student Rec Center": 1.5},
        "University Hall": {"McCarthy Hall": 2, "Carl's Jr": 8},
        "University Police": {"State College Parking": 1, "Golleher Alumni House": 1, },
        "Visual Arts": {"Parking I": 5, "Clayes Performing Arts Center": 2},

}
    
    gui.show_gui(adjacency_list) # pass adjacency list to the GUI

# Call main
if __name__ == "__main__":
    main()