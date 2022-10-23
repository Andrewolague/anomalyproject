The first portion of the project scriptsql.py was simply to generate 15000 rows of test data via faker
We are considering an empty string or "" in either first or last name as an anomaly 
We are also considering an address starting with "123" as an anomaly 
Proceed to run the python script to connect then open the command prompt                               Type "sqlite3" in the command prompt
Set mode to CSV to import data(note to set headers in first row beforehand if possible)                .mode csv
Set a path to the CSV containing the data then add a space with the following syntax follow along
                                                                                                      .import c:/sqlite/rogue_data.csv Nameoftable
Validate that the schema is correct for your CSV using .schema Nameoftable
Begin doing a simple query with small amount of results to validate that the data is correct
SELECT * FROM Nameoftable LIMIT 5;
Now set the output for our results of intended data of collecting anomalies                             .output results.csv
This should normally save in the same area that the python script is located
Final query for intended schema of firstname,lastname,address with table named Userdata
SELECT * FROM Userdata WHERE firstname='' OR lastname='' OR address LIKE '123%';
Total data was within a reasonable range of expected outcome with 1200 total records generated at 0.08 or 8% rogue data.
 