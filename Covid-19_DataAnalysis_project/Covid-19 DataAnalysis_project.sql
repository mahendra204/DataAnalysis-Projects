select * from covid_deaths 
select * from covid_vaccination 

---selecting the data which we are going to use

select top 1000 location,date,total_cases, new_cases,total_deaths, population from covid_deaths order by 1,2 

--Q: finding the total cases and total deaths location wise
select top 100 location,max(date) as date,max(total_cases) as total_cases,
max(total_deaths) as total_deaths
from covid_deaths group by location order by location

--Q: data related to india:
select top 1000 location,date,total_cases,total_deaths
from covid_deaths where location ='india' order by date desc


--Q:find the highest infection rate across all locations.
select location, population,max(total_cases) as highestinfectioncount, max((total_cases/population))*100 as 
percentage_infection from covid_deaths group by location, population order by percentage_infection desc

--Q: find the countries with highest death count per population.
select location, population, max(cast(total_deaths as int)) as higest_deaths, max((total_deaths/population))*100 
as percentage_deaths from covid_deaths where continent is not null group by location, population order by 
percentage_deaths desc

--Q:break down by each continent.
select continent, max(cast(total_deaths as int)) as total_deathscount 
from covid_deaths where continent is not null
group by continent order by total_deathscount desc


select location, max(cast(total_deaths as int)) as total_deathscount from covid_deaths where continent is null
group by location order by total_deathscount desc

--Q: write a query that returns continents with highest death count per population.
select continent, max(cast(total_deaths as int)) as total_deathcount from 
covid_deaths where continent is not null 
group by continent order by total_deathcount desc

--Q: find the numbers as global values

select date, sum(new_cases) as new_cases_across_globe, sum(cast(new_deaths as int)) as total_deaths
 from covid_deaths where continent is not null group by date order by 1,2 desc

 --Q: find the number of records are common with location and date finding it by applying join condition.
 select count(*) from covid_deaths d join 
 covid_vaccination v on d.location = v.location and d.date=v.date

  select * from covid_deaths d join 
 covid_vaccination v on d.location = v.location and d.date=v.date
 
 --Q: finding total populaiton vs vaccination
 select d.continent, d.location, d.date, d.population,v.new_vaccinations 
 from covid_deaths d join covid_vaccination v
 on d.date=v.date and d.location=v.location where d.continent is not null order by 2,3 

 --Q: applying window funtions to find the rank interms of new_vaccinations
 select d.continent, d.location, d.date, d.population, v.new_vaccinations, 
 sum(cast(v.new_vaccinations as int)) over(partition by d.location order by d.date)
  from covid_deaths d join covid_vaccination v on d.location=v.location and d.date =v.date 
 where d.continent is not null
 order by 2,3

 ---using cte method
--SET ANSI_WARNINGS OFF
with cte as ( select d.continent, d.location, d.date, d.population, v.new_vaccinations, 
 sum(cast(v.new_vaccinations as int)) over (partition by d.location order by d.location,d.date) as peoplevaccinated from covid_deaths d
 join covid_vaccination v on d.location=v.location and d.date=v.date where d.continent is not null)
 select * from cte
