Create DATABASE VirtualArtGallery;
Use VirtualArtGallery;
CREATE TABLE Artists (
    ArtistID INT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Biography TEXT,
    Nationality VARCHAR(100)
);
use VirtualArtGallery
CREATE TABLE Categories (
    CategoryID INT PRIMARY KEY,
    Name VARCHAR(100) 
);
select * from Categories
-- Create the Artworks table
CREATE TABLE Artworks (
    ArtworkID INT PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    ArtistID INT,
    CategoryID INT,
    Year INT,
    Description TEXT,
    ImageURL VARCHAR(255),
    FOREIGN KEY (ArtistID) REFERENCES Artists (ArtistID),
    FOREIGN KEY (CategoryID) REFERENCES Categories (CategoryID)
);

-- Create the Exhibitions table
CREATE TABLE Exhibitions (
    ExhibitionID INT PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    StartDate DATE,
    EndDate DATE,
    Description TEXT
);

-- Create a table to associate artworks with exhibitions
CREATE TABLE ExhibitionArtworks (
    ExhibitionID INT,
    ArtworkID INT,
    PRIMARY KEY (ExhibitionID, ArtworkID),
    FOREIGN KEY (ExhibitionID) REFERENCES Exhibitions (ExhibitionID),
    FOREIGN KEY (ArtworkID) REFERENCES Artworks (ArtworkID)
);
INSERT INTO Artists (ArtistID, Name, Biography, Nationality) VALUES
(1, 'Pablo Picasso', 'Renowned Spanish painter and sculptor.', 'Spanish'),
(2, 'Vincent van Gogh', 'Dutch post-impressionist painter.', 'Dutch'),
(3, 'Leonardo da Vinci', 'Italian polymath of the Renaissance.', 'Italian');


INSERT INTO Categories (CategoryID, Name) VALUES
(1, 'Painting'),
(2, 'Sculpture'),
(3, 'Photography');
USE VirtualArtGallery
INSERT INTO Artworks (ArtworkID, Title, ArtistID, CategoryID, Year, Description, ImageURL) VALUES
(1, 'Starry Night', 2, 1, 1889, 'A famous painting by Vincent van Gogh.', 'starry_night.jpg'),
(2, 'Mona Lisa', 3, 1, 1503, 'The iconic portrait by Leonardo da Vinci.', 'mona_lisa.jpg'),
(3, 'Guernica', 1, 1, 1937, 'Pablo Picasso''s powerful anti-war mural.', 'guernica.jpg');

INSERT INTO Exhibitions (ExhibitionID, Title, StartDate, EndDate, Description) VALUES
(1, 'Modern Art Masterpieces', '2023-01-01', '2023-03-01', 'A collection of modern art masterpieces'),
(2, 'Renaissance Art', '2023-04-01', '2023-06-01', 'A showcase of Renaissance art treasures.');
use VirtualArtGallery
INSERT INTO ExhibitionArtworks (ExhibitionID, ArtworkID) VALUES
(1, 1),
(1, 2),
(1, 3),
(2, 2);




--Q1

SELECT a.Name, COUNT(aw.ArtworkID) AS ArtworkCount
FROM Artists a
LEFT JOIN Artworks aw ON a.ArtistID = aw.ArtistID
GROUP BY a.Name
ORDER BY ArtworkCount DESC;


--Q2

SELECT aw.Title
FROM Artworks aw
JOIN Artists a ON aw.ArtistID = a.ArtistID
WHERE a.Nationality IN ('Spanish', 'Dutch')
ORDER BY aw.Year ASC;


--Q3
SELECT a.Name AS ArtistName, COUNT(aw.ArtworkID) AS NumberOfArtworks
FROM Artists a
JOIN Artworks aw ON a.ArtistID = aw.ArtistID
JOIN Categories c ON aw.CategoryID = c.CategoryID
WHERE c.Name = 'Painting'
GROUP BY a.Name;

--Q4
SELECT aw.Title AS ArtworkTitle, a.Name AS ArtistName, c.Name AS CategoryName
FROM Exhibitions e
JOIN ExhibitionArtworks ea ON e.ExhibitionID = ea.ExhibitionID
JOIN Artworks aw ON ea.ArtworkID = aw.ArtworkID
JOIN Artists a ON aw.ArtistID = a.ArtistID
JOIN Categories c ON aw.CategoryID = c.CategoryID
WHERE e.Title = 'Modern Art Masterpieces';



--Q5

SELECT a.Name
FROM Artists a
JOIN Artworks aw ON a.ArtistID = aw.ArtistID
GROUP BY a.Name
HAVING COUNT(aw.ArtworkID) > 2;

--Q6


select aw.Title from Artworks aw
 where aw.ArtworkID in
 
 (
	select ea.ArtworkID
	from ExhibitionArtworks ea 
	join Exhibitions e on ea.ExhibitionID = e.ExhibitionID
	where e.Title = 'Modern Art Masterpieces'
 )
 and aw.ArtworkID in
 (
	select ea.ArtworkID
	from ExhibitionArtworks ea 
	join Exhibitions e on ea.ExhibitionID = e.ExhibitionID
	where e.Title = 'Renaissance Art'
 );

--Q7
SELECT c.Name, COUNT(aw.ArtworkID) AS TotalArtworks
FROM Categories c
LEFT JOIN Artworks aw ON c.CategoryID = aw.CategoryID
GROUP BY c.Name;


--Q8
SELECT a.Name
FROM Artists a
JOIN Artworks aw ON a.ArtistID = aw.ArtistID
GROUP BY a.Name
HAVING COUNT(aw.ArtworkID) > 3;



--Q9
SELECT aw.Title
FROM Artworks aw
JOIN Artists a ON aw.ArtistID = a.ArtistID
WHERE a.Nationality = 'Spanish';


--Q10
SELECT e.Title
FROM Exhibitions e
JOIN ExhibitionArtworks ea ON e.ExhibitionID = ea.ExhibitionID
JOIN Artworks aw ON ea.ArtworkID = aw.ArtworkID
JOIN Artists a ON aw.ArtistID = a.ArtistID
WHERE a.Name = 'Vincent van Gogh'
AND e.ExhibitionID IN (
    SELECT e2.ExhibitionID
    FROM Exhibitions e2
    JOIN ExhibitionArtworks ea2 ON e2.ExhibitionID = ea2.ExhibitionID
    JOIN Artworks aw2 ON ea2.ArtworkID = aw2.ArtworkID
    JOIN Artists a2 ON aw2.ArtistID = a2.ArtistID
    WHERE a2.Name = 'Leonardo da Vinci'
)
GROUP BY e.Title;



--Q11
SELECT aw.Title
FROM Artworks aw
LEFT JOIN ExhibitionArtworks ea ON aw.ArtworkID = ea.ArtworkID
WHERE ea.ExhibitionID IS NULL;

--Q12
SELECT a.Name
FROM Artists a
JOIN Artworks aw ON a.ArtistID = aw.ArtistID
GROUP BY a.Name
HAVING COUNT(DISTINCT aw.CategoryID) = (SELECT COUNT(*) FROM Categories);
-- null


--Q13

SELECT c.Name, COUNT(aw.ArtworkID) AS TotalArtworks
FROM Categories c
LEFT JOIN Artworks aw ON c.CategoryID = aw.CategoryID
GROUP BY c.Name
ORDER BY TotalArtworks DESC;  




--Q14
SELECT a.Name
FROM Artists a
JOIN Artworks aw ON a.ArtistID = aw.ArtistID
GROUP BY a.Name
HAVING COUNT(aw.ArtworkID) > 2;

--Q15

SELECT c.Name, AVG(aw.Year) AS AverageYear
FROM Categories c
JOIN Artworks aw ON  aw.CategoryID = c.CategoryID
GROUP BY c.Name
HAVING COUNT(aw.ArtworkID) > 1;

--Q16
SELECT aw.Title
FROM Artworks aw
JOIN ExhibitionArtworks ea ON aw.ArtworkID = ea.ArtworkID
JOIN Exhibitions e ON ea.ExhibitionID = e.ExhibitionID
WHERE e.Title = 'Modern Art Masterpieces';


--Q17
SELECT c.Name
FROM Categories c
JOIN Artworks aw ON c.CategoryID = aw.CategoryID
GROUP BY c.Name
HAVING AVG(aw.Year) > (SELECT AVG(Year) FROM Artworks);



--Q18
SELECT aw.Title
FROM Artworks aw
LEFT JOIN ExhibitionArtworks ea ON aw.ArtworkID = ea.ArtworkID
WHERE ea.ExhibitionID IS NULL;


--Q19
SELECT DISTINCT a.Name
FROM Artists a
JOIN Artworks aw ON a.ArtistID = aw.ArtistID
WHERE aw.CategoryID = (SELECT CategoryID FROM Artworks WHERE Title = 'Mona Lisa');


--Q20
SELECT a.Name, COUNT(aw.ArtworkID) AS ArtworkCount
FROM Artists a
LEFT JOIN Artworks aw ON a.ArtistID = aw.ArtistID
GROUP BY a.Name
order by ArtworkCount DESC;
