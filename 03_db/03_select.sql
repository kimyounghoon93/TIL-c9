SELECT * FROM movies WHERE 상영시간 >= 150;
SELECT * FROM movies WHERE 장르 = '애니메이션';
SELECT * FROM movies WHERE 제작국가='덴마크' and 장르='애니메이션';
SELECT 영화이름, 누적관객수 FROM movies WHERE 누적관객수>=1000000 and 관람등급='청소년관람불가';
SELECT * FROM movies WHERE 개봉연도 BETWEEN 20000101 and 20091231;
SELECT DISTINCT 장르 FROM movies;