select * from covid_deaths 
select * from covid_vaccination 

---selecting the data which we are going to use

select top 1000 location,date,total_cases, new_cases,total_deaths, population from covid_deaths order by 1,2 

--Q: finding the total cases and total deaths location wise
select location,max(total_cases),max(total_deaths) from covid_deaths group by location order by location