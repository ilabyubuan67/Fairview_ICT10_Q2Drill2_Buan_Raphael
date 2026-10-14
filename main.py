from pyscript import document

Grade_7 = {   'Maggie Chiong', 'Mandy Cajanding','Mateo Salacup','Cianna Del Prado','Myka Dela Rosa'}

Grade_8 = {'Parminder Bhullar', 'Rafa Roncal','Wenzelvic Paragas'}

Grade_9 = {'Jan Cabading', 'Ian Salangsang','Jacqueline Tian'}

Grade_10 = {'Raphael Buan','Dustin Cunanan','Julia Bermudez'}

# Combine all four grade sets
Master_set = Grade_7 | Grade_8 | Grade_9 | Grade_10


def add_members(e):
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()

    # Combines the first and last
    fullname = first_name + " " + last_name

    # Add the new member using a set operator
    Final_result = Master_set | {fullname}

    # It sorts the members from a to z
    Member_list = "<br>".join(sorted(Final_result))

    # Basically Displays the member list
    document.getElementById("result").innerHTML = f"""<h3>All Science Club Members</h3>{Member_list}
        <hr>
        <h3>Total Members: {len(Final_result)}</h3> """