Date: 2013-04-17
Title: Fixing the high skilled immigration problem

It is an undeniable fact that immigrants play an important role in the tech industry not just in silicon valley but throughout the country. Be it a small startup with 20 people trying to innovate something or a big corporation with thousands of employees, it is very common to find people at various levels in an organization working on a visa. Every year on the 1st of April, 65000 H1B visas (an additional 20000 for those with advanced degrees from the US) are made available. There have been a number of proposals to increase this number substantially with reforms and there are bills [[1]](#fn1)[[2]](#fn2) in the senate which are in progress for this issue.  

These 85000 visas are in high demand and they are issued on a first come first served basis until the cap is reached. The exception is when more than 85000 applications are submitted with the first 5 days. This happened last in 2008 when the economy was booming and it has happened again. For the FY 2014, the number of applications submitted was more than the the number of visas available. USCIS made a [press release](http://www.uscis.gov/portal/site/uscis/menuitem.5af9bb95919f35e66f614176543f6d1a/?vgnextoid=c91dea8c9eadd310VgnVCM100000082ca60aRCRD&vgnextchannel=68439c7755cb9010VgnVCM10000045f3d6a1RCRD) stating that 124000 applications were received for the 85000 slots and they will be giving away those visa a random selection process aka the "Lottery". To resonate the impact of this situation, i just picked a couple of quotes from a discussion thread on Hacker News. 

>*I have a coworker who is an unbelievably talented and respected developer both at my company and in the open source community. He has been working on a student visa after he graduated from an Ivy League school in computer science last year*.

>*That the U.S. is even considering deporting him is batshit crazy to me*.

>*- [jdross](https://news.ycombinator.com/item?id=5514313)*

>*It is insane. Despite getting in by April 1st we're now waiting on the lottery results to see if our first engineering hire can stay in the country. It's going to be extremely disruptive both to him and to us if he can't stay. Stupid*.

>*-[acgourley](https://news.ycombinator.com/item?id=5514504)*

####Distribution of H1B Visas####

Even before thinking about bringing reforms to this broken system, it is important to understand where the visas go right now and how the system is being gamed. I am quoting some points from an answer on Quora which i wrote last year for the question ["H1B Visa: What effect will the 2013 H1B run-out have on the tech industry?"](http://www.quora.com/H1B-Visa-1/What-effect-will-the-2013-H1B-run-out-have-on-the-tech-industry/answer/Ram-Parthasarathy)


The rough split of where the H1B visa goes is as follows

- The big Indian outsourcing firms (tcs, infosys, cts, wipro etc) who want to bring their employees on cheap labor on a long term basis to their client sites. This category forms one of the biggest parts of the pie.
- The big tech companies like Microsoft, Google, FB and numerous other companies across different sectors who hire international students. Some of these visas will be applied under the 65000 general quota since the student wouldn't have graduated when the companies extend an offer. The degree certificate is needed to apply under the Master's quota (20000 visas).
- Tech consulting shops (a lot of fraudulent ones) get a large number of visas. They are listed as the employer in the visa but the person will generally be contracting for another company and the consulting shop generally takes a big cut from the consulting fees. This is one way how people who don't go to school in the US get their foot in the country.

USCIS makes all the H1B data publicly available every year and it is very evident that currently H1B is just being used as an outsourcing visa. There isn't a single "proper US company"[[3]](#fn3) in the top ten list. Microsoft corporation stands at number 11 with 1497 visas for the 2012 FY. This interesting [H1B data analysis](http://deepakbala.me/2012/08/26/analyzing-h1b-data-with-python-and-pandas/) by Deepak Bala also gives a very good perspective of the current state of affairs.

<div class = "center-img">

    <img alt ="H1B Top Employers" src = "/img/post-images/h1btop10.png"></img>
    <p> 
        Source : <a href="http://www.computerworld.com/s/article/9236732/The_data_shows_Top_H_1B_users_are_offshore_outsourcers">Computerworld</a>
    </p>
</div>

<div class = "center-img">

    <img alt ="H1B Top Companies" src = "/img/post-images/h1bcompanies.png"></img>
    <p> 
        Source : <a href="http://deepakbala.me/2012/08/26/analyzing-h1b-data-with-python-and-pandas/">Deepak Bala</a>
    </p>
</div>

####Definition of High Skilled Labor####

The big question in the minds of most people is if there is really a shortage of talent in the US forcing companies to hire internationals or is it an artificially created thing. There is definitely a storage of high skilled labor in technology but it is very hard to term what exactly constitutes a person as highly skilled. According to USCIS, it is someone who has a bachelor's degree in the relevant field and already has a job offer from a company who is willing to pay the person above the prevailing wage[[4]](#fn4) in that region. So, the following people are all classified as 'high skilled' and compete for the H1B in the same pool. There is no demarcation or a points based system followed by many other countries.

- a PhD from Standford working on Google's automated car
- a graduate with a master's degree in computer science working on Amazon's infrastructure 
- a computer engineering graduate building wearable electronic devices at a stealth silicon valley startup 
- the more common software engineer or analyst at small-medium sized businesses and fortune 500 companies
- a project lead from Wipro responsible for the operations of the onsite team at the client's venue
- an employee from infosys/cts/tcs testing and writing bug reports for a 20 year old mainframe system for a big box retailer. 

These 6 broad categories will mostly cover 90-95% of the applicant pool. In addition, a small percentage of physicians, medical residents and skilled professionals from non technology sectors also depend on the H1B visa. 

####Fixing the broken system####

Increasing the number of available visas isn't going to fix anything. In fact, a blind increase will make way for more outsourced cheap labor resulting in a situation worse than what we have right now.

Here are some suggestions to bring some sanity to the high skilled immigration problem. 

1. **Prevent companies who employ more than 50 percent of its employees in the United States in H-1B or L from obtaining more H1B visas.** In 2010, the Public Law 111-230[[5]](#fn5) was signed by President Obama which requires an additional fee of $2000 for every petition from such companies. This amount is really insignificant for multi-billion dollar corporations like TCS and Infosys working on long term multi-million dollar contracts for US clients. 

    This will not only stop the outsourcing shops from bringing in more cheap labor but also encourage them to hire locally. It could result in tens of thousands of new entry level technology jobs in the next 5 to 10 years. Most of these jobs are in testing and maintenance and it wouldn't take long to train entry level CS and IT graduates to be ready for the job. In my opinion, taking this step alone will alleviate the issue and move things forward in a nice way.  

2. **Implement a points based system** that gives more weightage to applicants with advanced degrees, higher income levels, small businesses etc. The UK Border Agency's [points based system](http://www.ukba.homeoffice.gov.uk/visas-immigration/working/whocanuse/) can be used as a good reference sheet.

3. **Allow H1B holders to start companies**. While it is theoretically possible for H1B visa holders to start companies it is not a very practical solution. The rule is that a H1B holder can start a company but she can't work for it. While it may sound totally illogical, there are strong reasons behind that rule. There needs to be a employer-employee relationship where the former should be able to terminate the employment of the latter and this relationship will vanish if the h1b holder is a major stakeholder in the business. 

    A more practical solution will be to allow the H1B holder to transfer the visa to an incubator or a VC firm for a short time period (12-24 months) and upon success or failure of the company, the visa can be transfered to the startup or to another company respectively. The VC firm or the incubator won't have any real obligation similar to a university's role in the post graduation OPT work authorization. If the startup is on a good track it will have a board established by then who will then be able to terminate the founder. This may sound a little too complicated but with a proper framework and rules it can be devised well.

    The probability of a new Google or Ebay is very very low but this will pave the way for thousands of new startups. 

4. **Split the available visas into two or three lots per year** and be flexible with the starting date. Currently the applications can be submitted starting only on April 1st and the starting date can only be after October 1st. 

    This is a big roadblock for companies who want to directly hire people living in other countries. If Quora finds a suitable candidate from India or Romania in the next code sprint or Google interviews at top universities in other countries and decides to extend an offer this summer, they cannot start working until October 1, 2014 unless they find a different visa which will allow the person to work inside the US. A year and a half (even 6-8 months) is a really long time for hiring decisions and this is especially true for startups. 

    While this may result in a significant administrative overhead for the USCIS, this will be very helpful for the companies. An additional fee if the application isn't submitted in the lot 1 is a possible solution.

5. **Substantially increase the fee for companies that have more than 500 employees on visas**. Microsoft proposed a [$10000 additional fee](http://www.geekwire.com/2013/h1b-visas-tech-companies-divided-plan-higher-fees/) for H1Bs and a $15000 fee for green cards. Most employers will be ready to pay this fee and this will be a nice additional revenue source for the government.

6. Have a more realistic prevailing wage[[4]](#fn4) requirement or set a new minimum wage band for H1B applicants. This will ensure that existing tech workers aren't [displaced by h1b workers](http://www.motherjones.com/politics/2013/02/silicon-valley-h1b-visas-hurt-tech-workers) at a lower wage.  

7. **Implement stringent checks to prevent misuse and fraud**. There are a number of bodyshops who obtain h1b visas, serve as a middle man and take a cut. This is bad for the client, bad for the employee and bad for everyone involved except the bodyshop. While there are many genuine consulting businesses utilizing visa workers, the operations of a majority of these consulting companies are fraudulent. The USCIS is very well aware of this practice but has failed to take any action.

PS: I have been writing this post in parts over the past 3-4 weeks and a few nice developments have started in the meantime. Most notable one is the [fwd.us](http://fwd.us) initiative from many well known tech leaders including Mark Zuckerberg. The gang of eight's new immigration bill also has some good proposals.

<a name = "fn1">[1]</a> [I-Squared Act of 2013](http://www.govtrack.us/congress/bills/113/s169#overview) is a proposal for increasing the visa limits and also providing work authorization for dependents of the visa holder.

<a name = "fn2">[2]</a> [H-1B and L-1 Visa Reform Act of 2013](http://www.govtrack.us/congress/bills/113/s600/text) proposes modifications of the requirements and also the review procedure.

<a name = "fn3">[3]</a> The top 10 in that list are registered US companies but they are primarily Indian outsourcing companies with a presence in the United States.

<a name = "fn4">[4]</a> Prevailing wage is a minimum annual or hourly wage required for a H1B worker. This wage requirement is generally quoted from [Foreign Labor Certification Data Center](http://www.flcdatacenter.com/OESQuick.aspx). While some of the quoted wages are inline with the market rates, there are certainly loopholes where a software engineer who gets paid 75K in the bay area is eligible for a H1B visa which is definitely in the lowest end of the bracket.

<a name = "fn5">[5]</a> [Public Law 111-230](http://www.uscis.gov/USCIS/Laws/Memoranda/2011/Public_Law_111-230_Memo.pdf) (pdf) increased the fee for outsourcing companies by $2000 for every petition. 








