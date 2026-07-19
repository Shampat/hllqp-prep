
import json

output = "app/src/main/assets/questions/ethics_questions.json"

questions = []

def add_question(
    qid,
    topic,
    difficulty,
    question,
    options,
    correct,
    explanation
):
    questions.append({
        "id": qid,
        "moduleId": "ethics",
        "moduleName": "Ethics & Professional Conduct",
        "topic": topic,
        "difficulty": difficulty,
        "question": question,
        "options": options,
        "correctAnswer": correct,
        "explanation": explanation
    })


add_question(1,"Professional Conduct","Easy",
"What is the primary responsibility of an insurance advisor?",
[
"Act in the client's best interest",
"Maximize commissions",
"Guarantee investment returns",
"Avoid documenting advice"
],
0,
"Advisors must act ethically and in the client's best interest.")


add_question(2,"Professional Conduct","Easy",
"An advisor should provide:",
[
"Accurate and complete information",
"Only positive information",
"Hidden details",
"Guaranteed outcomes"
],
0,
"Clients need complete and accurate information.")


add_question(3,"Ethics","Easy",
"Ethical behaviour requires:",
[
"Honesty and integrity",
"Misleading statements",
"Hidden fees",
"False promises"
],
0,
"Integrity is a core ethical requirement.")


add_question(4,"Client Needs","Medium",
"Suitable recommendations are based on:",
[
"Client circumstances and objectives",
"Highest commission",
"Advisor preference",
"Sales targets"
],
0,
"Recommendations must be suitable for the client.")


add_question(5,"Disclosure","Medium",
"An advisor should disclose:",
[
"Relevant information about products and conflicts",
"Only benefits",
"Only fees",
"Nothing"
],
0,
"Proper disclosure supports informed decisions.")



add_question(6,"Conflicts of Interest","Easy",
"A conflict of interest occurs when:",
[
"Personal interests may affect professional judgment",
"Clients ask questions",
"Policies are explained",
"Documents are completed"
],
0,
"Conflicts can affect objective advice.")


add_question(7,"Conflicts of Interest","Medium",
"An advisor should handle conflicts by:",
[
"Disclosing them appropriately",
"Hiding them",
"Ignoring them",
"Transferring them to clients"
],
0,
"Disclosure helps clients make informed decisions.")


add_question(8,"Client Needs","Easy",
"Before recommending a product, an advisor should understand:",
[
"Client needs and objectives",
"Only commission rates",
"Only product popularity",
"Only market trends"
],
0,
"Recommendations require understanding the client.")


add_question(9,"Client Needs","Medium",
"A fact-finding process helps determine:",
[
"Client financial circumstances",
"Advisor income",
"Sales targets",
"Advertising plans"
],
0,
"Fact finding supports suitable recommendations.")


add_question(10,"Professional Conduct","Easy",
"Professional conduct requires:",
[
"Honesty and fairness",
"Misleading statements",
"Hidden information",
"Pressure sales"
],
0,
"Ethical conduct requires honesty and fairness.")


add_question(11,"Disclosure","Easy",
"Product information should be:",
[
"Clear and understandable",
"Hidden",
"Changed frequently",
"Only verbal"
],
0,
"Clients need clear information.")


add_question(12,"Disclosure","Medium",
"Material information includes:",
[
"Important facts affecting a decision",
"Personal opinions only",
"Marketing slogans",
"Unrelated details"
],
0,
"Material facts influence decisions.")


add_question(13,"Privacy","Easy",
"Client information should be:",
[
"Kept confidential",
"Shared publicly",
"Sold to others",
"Ignored"
],
0,
"Client privacy must be protected.")


add_question(14,"Privacy","Medium",
"Personal information may be used:",
[
"Only for appropriate purposes",
"Without permission",
"Publicly",
"For personal benefit"
],
0,
"Information must be handled properly.")


add_question(15,"Documentation","Easy",
"Documentation helps show:",
[
"Advice and decisions made",
"Only sales results",
"Only commissions",
"Only product names"
],
0,
"Proper records support accountability.")


add_question(16,"Documentation","Medium",
"Advisor records should be:",
[
"Accurate and complete",
"Missing details",
"Destroyed immediately",
"Based on memory only"
],
0,
"Good records are accurate and complete.")


add_question(17,"Client Communication","Easy",
"An advisor should communicate:",
[
"Clearly and honestly",
"With guarantees",
"Only through advertisements",
"Without explanations"
],
0,
"Clear communication builds trust.")


add_question(18,"Client Communication","Medium",
"An advisor should avoid:",
[
"Misleading clients",
"Explaining risks",
"Reviewing needs",
"Answering questions"
],
0,
"Misleading clients violates ethical standards.")


add_question(19,"Suitability","Easy",
"Suitability means:",
[
"Product matches client needs",
"Product has highest commission",
"Product is most expensive",
"Product is most popular"
],
0,
"Recommendations should fit client circumstances.")


add_question(20,"Suitability","Medium",
"A suitable recommendation considers:",
[
"Objectives, risk, and circumstances",
"Only advisor preference",
"Only commissions",
"Only sales goals"
],
0,
"Suitability requires complete consideration.")


add_question(21,"Professional Conduct","Easy",
"An advisor should act:",
[
"With integrity",
"With deception",
"Without records",
"Without disclosure"
],
0,
"Integrity is a fundamental ethical principle.")


add_question(22,"Professional Conduct","Medium",
"Ethical advisors place importance on:",
[
"Client interests",
"Personal gain only",
"Sales pressure",
"Hidden benefits"
],
0,
"Client interests should be prioritized.")


add_question(23,"Compliance","Easy",
"Compliance means:",
[
"Following applicable rules and regulations",
"Ignoring laws",
"Avoiding records",
"Removing disclosure"
],
0,
"Compliance requires following requirements.")


add_question(24,"Compliance","Medium",
"Regulatory requirements exist to:",
[
"Protect clients and maintain standards",
"Increase commissions",
"Remove documentation",
"Prevent advice"
],
0,
"Regulation protects consumers.")


add_question(25,"Ethics","Medium",
"Ethical decision-making should consider:",
[
"Client impact and professional duties",
"Only personal benefit",
"Only sales results",
"Only market conditions"
],
0,
"Ethical choices consider responsibilities and impact.")



add_question(26,"Client Interests","Easy",
"An advisor's first priority should be:",
[
"Client interests",
"Personal commission",
"Sales targets",
"Product popularity"
],
0,
"Ethical advisors prioritize clients.")


add_question(27,"Client Interests","Medium",
"Putting clients first means:",
[
"Considering their goals and circumstances",
"Choosing the highest fee product",
"Ignoring their concerns",
"Making decisions without them"
],
0,
"Client-focused advice considers individual needs.")


add_question(28,"Professional Conduct","Easy",
"An advisor should avoid:",
[
"False or misleading statements",
"Clear explanations",
"Proper documentation",
"Disclosure"
],
0,
"Misleading statements violate professional standards.")


add_question(29,"Professional Conduct","Medium",
"Professional integrity requires:",
[
"Honest and responsible behaviour",
"Hidden information",
"Pressure tactics",
"False promises"
],
0,
"Integrity requires responsible actions.")


add_question(30,"Confidentiality","Easy",
"Confidential client information should be:",
[
"Protected",
"Shared freely",
"Posted publicly",
"Sold"
],
0,
"Confidentiality protects client information.")


add_question(31,"Confidentiality","Medium",
"Client information may be disclosed:",
[
"When authorized or legally required",
"Whenever requested by anyone",
"For personal benefit",
"Without reason"
],
0,
"Disclosure must be appropriate.")


add_question(32,"Communication","Easy",
"Good communication includes:",
[
"Listening and explaining clearly",
"Using pressure",
"Hiding details",
"Making guarantees"
],
0,
"Communication requires clarity.")


add_question(33,"Communication","Medium",
"An advisor should explain:",
[
"Risks, benefits, and limitations",
"Only benefits",
"Only costs",
"Only guarantees"
],
0,
"Balanced information supports decisions.")


add_question(34,"Conflict Management","Easy",
"Conflicts should be:",
[
"Managed appropriately",
"Hidden",
"Ignored",
"Encouraged"
],
0,
"Conflicts require proper handling.")


add_question(35,"Conflict Management","Medium",
"Conflict disclosure helps:",
[
"Clients understand potential bias",
"Increase commissions",
"Remove regulations",
"Avoid documentation"
],
0,
"Disclosure supports transparency.")


add_question(36,"Compliance","Easy",
"Rules and regulations help:",
[
"Protect clients",
"Increase misleading sales",
"Remove responsibility",
"Avoid advice"
],
0,
"Regulation protects consumers.")


add_question(37,"Compliance","Medium",
"An advisor should remain:",
[
"Up to date with requirements",
"Unaware of rules",
"Independent of laws",
"Without records"
],
0,
"Professionals must understand requirements.")


add_question(38,"Documentation","Easy",
"Records should reflect:",
[
"Important advice provided",
"Only sales numbers",
"Only fees",
"Only signatures"
],
0,
"Documentation supports accountability.")


add_question(39,"Documentation","Medium",
"Good documentation protects:",
[
"Clients and advisors",
"Only companies",
"Only salespeople",
"Only regulators"
],
0,
"Records provide evidence of proper advice.")


add_question(40,"Suitability","Easy",
"Suitability analysis considers:",
[
"Client needs",
"Advisor commission",
"Sales goals",
"Product popularity"
],
0,
"Suitability is client focused.")


add_question(41,"Suitability","Medium",
"Risk tolerance is important because:",
[
"Clients have different comfort levels with risk",
"All clients are identical",
"Risk never matters",
"Products are always equal"
],
0,
"Risk tolerance affects recommendations.")


add_question(42,"Ethics","Easy",
"Ethical advisors should be:",
[
"Trustworthy",
"Misleading",
"Secretive",
"Careless"
],
0,
"Trust is essential in advice.")


add_question(43,"Ethics","Medium",
"An ethical dilemma occurs when:",
[
"Values or duties conflict",
"Rules are clear",
"Documents are complete",
"Clients agree"
],
0,
"Dilemmas involve competing responsibilities.")


add_question(44,"Client Relationships","Easy",
"Trust is built through:",
[
"Honest service",
"Hidden information",
"Pressure tactics",
"False claims"
],
0,
"Honesty builds trust.")


add_question(45,"Client Relationships","Medium",
"Long-term client relationships require:",
[
"Integrity and communication",
"Only sales",
"Only commissions",
"Only product changes"
],
0,
"Relationships depend on ethical behaviour.")


add_question(46,"Professional Standards","Easy",
"A professional advisor should:",
[
"Follow ethical standards",
"Ignore rules",
"Hide conflicts",
"Guarantee results"
],
0,
"Standards guide professional behaviour.")


add_question(47,"Professional Standards","Medium",
"Professional standards exist to:",
[
"Maintain public confidence",
"Increase pressure sales",
"Remove responsibility",
"Reduce disclosure"
],
0,
"Standards protect the profession and clients.")


add_question(48,"Disclosure","Easy",
"Disclosure allows clients to:",
[
"Make informed decisions",
"Avoid all risks",
"Guarantee returns",
"Remove contracts"
],
0,
"Information helps informed choices.")


add_question(49,"Disclosure","Medium",
"An advisor should disclose:",
[
"Relevant conflicts and limitations",
"Only positive features",
"Only commissions",
"Nothing"
],
0,
"Disclosure must be complete and relevant.")


add_question(50,"Ethics","Medium",
"Ethical advice is based on:",
[
"Honesty, fairness, and client needs",
"Sales pressure",
"Personal gain",
"Hidden information"
],
0,
"Ethical advice follows professional principles.")



add_question(51,"Professional Conduct","Easy",
"An advisor should provide advice that is:",
[
"Fair and objective",
"Based on personal benefit",
"Misleading",
"Hidden"
],
0,
"Advice should be fair and objective.")


add_question(52,"Professional Conduct","Medium",
"Objectivity means:",
[
"Making decisions without improper bias",
"Choosing highest commission",
"Ignoring client needs",
"Following sales pressure"
],
0,
"Objectivity supports ethical advice.")


add_question(53,"Client Needs","Easy",
"A client profile helps determine:",
[
"Appropriate recommendations",
"Commission amounts",
"Advertising plans",
"Sales targets"
],
0,
"Client profiles support suitability.")


add_question(54,"Client Needs","Medium",
"Important client information includes:",
[
"Goals, circumstances, and risk tolerance",
"Only age",
"Only income",
"Only product preference"
],
0,
"Complete information supports proper advice.")


add_question(55,"Risk","Easy",
"Risk tolerance describes:",
[
"Ability and willingness to accept risk",
"Guaranteed returns",
"Tax level",
"Commission amount"
],
0,
"Risk tolerance affects recommendations.")


add_question(56,"Risk","Medium",
"An advisor should explain:",
[
"Possible risks and outcomes",
"Only positive results",
"Guaranteed profits",
"Hidden conditions"
],
0,
"Clients need balanced information.")


add_question(57,"Compliance","Easy",
"Compliance requires:",
[
"Following applicable laws and rules",
"Ignoring regulations",
"Avoiding records",
"Hiding information"
],
0,
"Compliance ensures proper practices.")


add_question(58,"Compliance","Medium",
"Failure to follow rules may result in:",
[
"Disciplinary action",
"Guaranteed success",
"More commissions",
"Less responsibility"
],
0,
"Non-compliance can have consequences.")


add_question(59,"Privacy","Easy",
"Privacy protection means:",
[
"Safeguarding client information",
"Sharing information freely",
"Publishing records",
"Ignoring consent"
],
0,
"Privacy protects client information.")


add_question(60,"Privacy","Medium",
"Client consent is important when:",
[
"Using personal information",
"Choosing advertising",
"Setting commissions",
"Predicting markets"
],
0,
"Consent supports proper information use.")


add_question(61,"Documentation","Easy",
"Documentation should be:",
[
"Accurate",
"False",
"Incomplete",
"Unnecessary"
],
0,
"Accurate records are required.")


add_question(62,"Documentation","Medium",
"Keeping records helps demonstrate:",
[
"Proper advice process",
"Only sales volume",
"Only profits",
"Only marketing"
],
0,
"Records show how advice was provided.")


add_question(63,"Client Communication","Easy",
"An advisor should answer client questions:",
[
"Clearly and honestly",
"With guarantees",
"Avoiding details",
"Without explanation"
],
0,
"Clear answers support understanding.")


add_question(64,"Client Communication","Medium",
"Effective communication requires:",
[
"Listening to client concerns",
"Ignoring questions",
"Using pressure",
"Hiding risks"
],
0,
"Listening is part of good advice.")


add_question(65,"Conflicts of Interest","Easy",
"A conflict may occur when:",
[
"Personal interests affect advice",
"Clients ask questions",
"Policies are reviewed",
"Records are updated"
],
0,
"Conflicts can affect judgment.")


add_question(66,"Conflicts of Interest","Medium",
"Managing conflicts requires:",
[
"Disclosure and proper controls",
"Hiding information",
"Ignoring issues",
"Removing clients"
],
0,
"Conflicts must be handled responsibly.")


add_question(67,"Ethics","Easy",
"Ethical behaviour includes:",
[
"Respect and honesty",
"Deception",
"Pressure",
"False promises"
],
0,
"Ethics requires honest conduct.")


add_question(68,"Ethics","Medium",
"Ethical decisions consider:",
[
"Impact on clients",
"Only personal benefit",
"Only sales",
"Only commissions"
],
0,
"Ethical choices consider client impact.")


add_question(69,"Client Relationships","Easy",
"Client trust is maintained through:",
[
"Consistent ethical behaviour",
"Hidden information",
"False guarantees",
"Pressure tactics"
],
0,
"Trust depends on ethical actions.")


add_question(70,"Client Relationships","Medium",
"A strong relationship requires:",
[
"Communication and transparency",
"Only sales",
"Only product changes",
"Only fees"
],
0,
"Transparency builds relationships.")


add_question(71,"Professional Standards","Easy",
"Professional standards promote:",
[
"Quality and ethical service",
"Misleading practices",
"Hidden conflicts",
"Poor records"
],
0,
"Standards guide professional behaviour.")


add_question(72,"Professional Standards","Medium",
"Maintaining standards helps:",
[
"Protect the public",
"Increase pressure",
"Avoid responsibility",
"Remove disclosure"
],
0,
"Standards protect consumers.")


add_question(73,"Suitability","Easy",
"Suitability requires matching:",
[
"Products to client needs",
"Products to commissions",
"Products to advertising",
"Products to popularity"
],
0,
"Recommendations must fit clients.")


add_question(74,"Suitability","Medium",
"An unsuitable recommendation may:",
[
"Harm the client",
"Guarantee success",
"Remove risk",
"Improve every outcome"
],
0,
"Unsuitable advice can negatively affect clients.")


add_question(75,"Professional Conduct","Medium",
"An advisor demonstrates professionalism by:",
[
"Acting ethically and responsibly",
"Guaranteeing returns",
"Hiding limitations",
"Ignoring rules"
],
0,
"Professionalism requires ethical behaviour.")



add_question(76,"Disclosure","Easy",
"Disclosure helps clients understand:",
[
"Important product information",
"Only sales goals",
"Only commissions",
"Only advertisements"
],
0,
"Disclosure supports informed decisions.")


add_question(77,"Disclosure","Medium",
"An advisor must disclose:",
[
"Relevant information affecting the client",
"Only positive features",
"Only guarantees",
"Nothing"
],
0,
"Relevant information must be provided.")


add_question(78,"Client Interests","Easy",
"Acting in the client's best interest means:",
[
"Putting client needs first",
"Maximizing advisor income",
"Ignoring objectives",
"Using pressure"
],
0,
"Client needs should guide advice.")


add_question(79,"Client Interests","Medium",
"Client-focused advice avoids:",
[
"Conflicts and unsuitable recommendations",
"Clear communication",
"Documentation",
"Reviews"
],
0,
"Ethical advice avoids unsuitable practices.")


add_question(80,"Professional Conduct","Easy",
"An advisor should be accountable for:",
[
"Professional actions",
"Market performance",
"Government decisions",
"Client choices only"
],
0,
"Advisors are responsible for their conduct.")


add_question(81,"Professional Conduct","Medium",
"Accountability requires:",
[
"Taking responsibility for advice",
"Avoiding records",
"Blaming clients",
"Hiding mistakes"
],
0,
"Professionals accept responsibility.")


add_question(82,"Privacy","Easy",
"Client records should be:",
[
"Securely maintained",
"Publicly available",
"Shared freely",
"Destroyed immediately"
],
0,
"Records must be protected.")


add_question(83,"Privacy","Medium",
"Unauthorized sharing of client information is:",
[
"Improper",
"Required",
"Professional",
"Recommended"
],
0,
"Privacy rules restrict improper sharing.")


add_question(84,"Compliance","Easy",
"Regulations exist to:",
[
"Protect clients",
"Increase sales pressure",
"Remove ethics",
"Reduce information"
],
0,
"Regulations protect consumers.")


add_question(85,"Compliance","Medium",
"Following regulations demonstrates:",
[
"Professional responsibility",
"Poor service",
"Hidden practices",
"Personal gain"
],
0,
"Compliance is part of professionalism.")


add_question(86,"Ethics","Easy",
"Integrity means:",
[
"Doing the right thing",
"Maximizing profit",
"Hiding facts",
"Ignoring rules"
],
0,
"Integrity is ethical behaviour.")


add_question(87,"Ethics","Medium",
"An ethical advisor should avoid:",
[
"Misrepresentation",
"Honest explanations",
"Client reviews",
"Documentation"
],
0,
"Misrepresentation violates ethics.")


add_question(88,"Client Communication","Easy",
"Communication should be:",
[
"Clear and understandable",
"Confusing",
"Hidden",
"Misleading"
],
0,
"Clients need clear information.")


add_question(89,"Client Communication","Medium",
"An advisor should explain:",
[
"Benefits, risks, and limitations",
"Only benefits",
"Only costs",
"Only guarantees"
],
0,
"Balanced explanations are required.")


add_question(90,"Conflicts of Interest","Easy",
"Conflicts of interest should be:",
[
"Identified and managed",
"Hidden",
"Ignored",
"Encouraged"
],
0,
"Conflicts require proper management.")


add_question(91,"Conflicts of Interest","Medium",
"Disclosure of conflicts promotes:",
[
"Transparency",
"Misleading advice",
"Pressure sales",
"Hidden benefits"
],
0,
"Transparency supports trust.")


add_question(92,"Suitability","Easy",
"Suitability depends on:",
[
"Client circumstances",
"Advisor preference",
"Highest commission",
"Product popularity"
],
0,
"Suitability is client specific.")


add_question(93,"Suitability","Medium",
"Before recommending, an advisor should:",
[
"Assess client information",
"Ignore objectives",
"Choose randomly",
"Focus only on fees"
],
0,
"Assessment supports suitable advice.")


add_question(94,"Documentation","Easy",
"Records should show:",
[
"Reasoning behind recommendations",
"Only product names",
"Only signatures",
"Only fees"
],
0,
"Documentation explains advice decisions.")


add_question(95,"Documentation","Medium",
"Good records support:",
[
"Accountability and compliance",
"Hidden practices",
"False claims",
"Poor advice"
],
0,
"Records demonstrate proper conduct.")


add_question(96,"Professional Standards","Easy",
"Professional standards help maintain:",
[
"Public confidence",
"Hidden information",
"Poor service",
"Conflicts"
],
0,
"Standards protect trust in the profession.")


add_question(97,"Professional Standards","Medium",
"A professional advisor should continue:",
[
"Learning and improving knowledge",
"Ignoring changes",
"Avoiding rules",
"Stopping education"
],
0,
"Continuous learning supports competence.")


add_question(98,"Client Relationships","Easy",
"Respecting clients includes:",
[
"Listening and responding appropriately",
"Ignoring concerns",
"Using pressure",
"Hiding information"
],
0,
"Respect improves client relationships.")


add_question(99,"Client Relationships","Medium",
"Trust is strengthened by:",
[
"Honesty and transparency",
"False promises",
"Hidden conflicts",
"Pressure tactics"
],
0,
"Transparency builds trust.")


add_question(100,"Ethics","Medium",
"Ethical advice combines:",
[
"Integrity, competence, and client focus",
"Sales pressure only",
"Personal benefit only",
"Hidden information"
],
0,
"Ethical advice requires professional principles.")



add_question(101,"Competence","Easy",
"An advisor should maintain:",
[
"Professional knowledge and skills",
"Only sales ability",
"Personal opinions",
"Marketing skills only"
],
0,
"Competence requires knowledge and skills.")


add_question(102,"Competence","Medium",
"Continuing education helps advisors:",
[
"Remain knowledgeable",
"Avoid regulations",
"Guarantee returns",
"Remove responsibility"
],
0,
"Education supports professional competence.")


add_question(103,"Professional Conduct","Easy",
"An advisor should be:",
[
"Reliable and trustworthy",
"Misleading",
"Secretive",
"Careless"
],
0,
"Trustworthiness is essential.")


add_question(104,"Professional Conduct","Medium",
"Professional behaviour includes:",
[
"Respecting ethical obligations",
"Ignoring clients",
"Hiding information",
"Making false promises"
],
0,
"Ethical obligations guide behaviour.")


add_question(105,"Client Needs","Easy",
"Understanding clients helps provide:",
[
"Suitable advice",
"Maximum commissions",
"Random products",
"Guaranteed outcomes"
],
0,
"Understanding needs supports suitability.")


add_question(106,"Client Needs","Medium",
"Client goals should be:",
[
"Considered in recommendations",
"Ignored",
"Replaced by sales goals",
"Hidden"
],
0,
"Recommendations should reflect goals.")


add_question(107,"Risk","Easy",
"Risk disclosure helps clients:",
[
"Understand possible outcomes",
"Guarantee profits",
"Remove all risks",
"Avoid contracts"
],
0,
"Risk information supports decisions.")


add_question(108,"Risk","Medium",
"An advisor should explain:",
[
"Potential risks and limitations",
"Only benefits",
"Only guarantees",
"Only returns"
],
0,
"Balanced disclosure is required.")


add_question(109,"Conflicts of Interest","Easy",
"A conflict should be disclosed when it:",
[
"May affect advice",
"Never exists",
"Benefits the advisor only",
"Is hidden"
],
0,
"Relevant conflicts must be disclosed.")


add_question(110,"Conflicts of Interest","Medium",
"Managing conflicts protects:",
[
"Client trust",
"Sales targets",
"Commissions",
"Advertising"
],
0,
"Proper management protects relationships.")


add_question(111,"Privacy","Easy",
"Privacy obligations apply to:",
[
"Client personal information",
"Market prices",
"Advertising",
"Commission rates"
],
0,
"Privacy focuses on personal information.")


add_question(112,"Privacy","Medium",
"Client information should only be accessed by:",
[
"Authorized persons",
"Anyone interested",
"Public sources",
"Competitors"
],
0,
"Access should be controlled.")


add_question(113,"Compliance","Easy",
"Compliance records should be:",
[
"Maintained properly",
"Destroyed immediately",
"Hidden",
"Optional"
],
0,
"Records support compliance.")


add_question(114,"Compliance","Medium",
"Non-compliance can:",
[
"Damage professional standing",
"Guarantee success",
"Improve advice",
"Remove duties"
],
0,
"Failure to comply has consequences.")


add_question(115,"Disclosure","Easy",
"Clear disclosure allows clients to:",
[
"Make informed choices",
"Avoid all decisions",
"Guarantee results",
"Ignore risks"
],
0,
"Disclosure supports informed decisions.")


add_question(116,"Disclosure","Medium",
"An advisor should not:",
[
"Hide important information",
"Explain products",
"Discuss risks",
"Answer questions"
],
0,
"Important information cannot be hidden.")


add_question(117,"Ethics","Easy",
"Ethical behaviour builds:",
[
"Trust",
"Confusion",
"Pressure",
"Misunderstanding"
],
0,
"Ethics builds client trust.")


add_question(118,"Ethics","Medium",
"Ethical decisions should consider:",
[
"Consequences for clients",
"Only profit",
"Only sales",
"Only convenience"
],
0,
"Ethics considers client impact.")


add_question(119,"Documentation","Easy",
"Advice records should be:",
[
"Complete and accurate",
"Optional",
"Incorrect",
"Unclear"
],
0,
"Records must be reliable.")


add_question(120,"Documentation","Medium",
"Documentation demonstrates:",
[
"Professional process",
"Personal gain",
"Marketing strategy",
"Sales pressure"
],
0,
"Documentation shows how advice was provided.")


add_question(121,"Client Relationships","Easy",
"Client trust depends on:",
[
"Honest interactions",
"Hidden information",
"False claims",
"Pressure"
],
0,
"Honesty supports trust.")


add_question(122,"Client Relationships","Medium",
"Maintaining relationships requires:",
[
"Transparency and communication",
"Only selling",
"Only advertising",
"Ignoring feedback"
],
0,
"Good relationships require communication.")


add_question(123,"Suitability","Easy",
"A suitable recommendation should:",
[
"Meet client needs",
"Maximize commission",
"Ignore objectives",
"Be random"
],
0,
"Suitability is client focused.")


add_question(124,"Suitability","Medium",
"Unsuitable advice may:",
[
"Create harm for clients",
"Guarantee returns",
"Remove risk",
"Improve every outcome"
],
0,
"Unsuitable recommendations can harm clients.")


add_question(125,"Competence","Medium",
"A competent advisor demonstrates:",
[
"Knowledge and professional judgment",
"Only sales ability",
"Guaranteed results",
"Hidden practices"
],
0,
"Competence requires knowledge and judgment.")



add_question(151,"Professional Conduct","Easy",
"An advisor should avoid:",
[
"Misleading clients",
"Explaining products",
"Keeping records",
"Disclosing information"
],
0,
"Misleading clients violates professional duties.")


add_question(152,"Professional Conduct","Medium",
"Professional judgement requires:",
[
"Knowledge and ethical reasoning",
"Only sales skills",
"Personal benefit",
"Ignoring rules"
],
0,
"Judgement combines knowledge and ethics.")


add_question(153,"Client Interests","Easy",
"Client interests should be considered:",
[
"Before making recommendations",
"After selling products",
"Only during complaints",
"Never"
],
0,
"Client interests guide recommendations.")


add_question(154,"Client Interests","Medium",
"Putting clients first requires:",
[
"Understanding their goals",
"Maximizing commissions",
"Using pressure",
"Hiding limitations"
],
0,
"Client goals should guide advice.")


add_question(155,"Disclosure","Easy",
"Disclosure should be:",
[
"Timely and complete",
"Hidden",
"Delayed intentionally",
"Unnecessary"
],
0,
"Clients need timely information.")


add_question(156,"Disclosure","Medium",
"Incomplete disclosure may:",
[
"Prevent informed decisions",
"Guarantee success",
"Remove risks",
"Improve advice"
],
0,
"Missing information can harm decisions.")


add_question(157,"Compliance","Easy",
"Compliance procedures help:",
[
"Ensure proper practices",
"Avoid responsibilities",
"Hide information",
"Increase conflicts"
],
0,
"Procedures support compliance.")


add_question(158,"Compliance","Medium",
"Following regulations demonstrates:",
[
"Professional responsibility",
"Poor judgement",
"Hidden activity",
"Lack of knowledge"
],
0,
"Compliance is a professional obligation.")


add_question(159,"Privacy","Easy",
"Protecting privacy means:",
[
"Safeguarding client data",
"Sharing freely",
"Posting publicly",
"Ignoring consent"
],
0,
"Privacy requires protection.")


add_question(160,"Privacy","Medium",
"Client information should be:",
[
"Collected and used appropriately",
"Used for personal gain",
"Shared without reason",
"Ignored"
],
0,
"Information must be handled properly.")


add_question(161,"Risk","Easy",
"Risk information should be:",
[
"Explained clearly",
"Hidden",
"Removed",
"Guaranteed"
],
0,
"Clients need clear risk explanations.")


add_question(162,"Risk","Medium",
"Risk discussions help clients:",
[
"Make informed choices",
"Guarantee profits",
"Avoid all decisions",
"Remove contracts"
],
0,
"Understanding risk supports choices.")


add_question(163,"Suitability","Easy",
"Suitable advice considers:",
[
"Client situation",
"Advisor income",
"Sales goals",
"Advertising"
],
0,
"Suitability is client focused.")


add_question(164,"Suitability","Medium",
"An advisor should recommend products that:",
[
"Fit client needs",
"Pay the highest commission",
"Are most expensive",
"Are most popular"
],
0,
"Recommendations should be appropriate.")


add_question(165,"Documentation","Easy",
"Advisor records should be:",
[
"Accurate",
"False",
"Optional",
"Missing"
],
0,
"Accurate records are required.")


add_question(166,"Documentation","Medium",
"Documentation supports:",
[
"Accountability",
"Hidden decisions",
"Poor service",
"Misrepresentation"
],
0,
"Records demonstrate responsible conduct.")


add_question(167,"Communication","Easy",
"Good communication builds:",
[
"Understanding",
"Confusion",
"Pressure",
"Distrust"
],
0,
"Clear communication improves understanding.")


add_question(168,"Communication","Medium",
"Advisors should explain information in a way clients:",
[
"Can understand",
"Cannot question",
"Must accept",
"Cannot review"
],
0,
"Information should be understandable.")


add_question(169,"Ethics","Easy",
"Ethical advisors demonstrate:",
[
"Integrity",
"Deception",
"Bias",
"Negligence"
],
0,
"Integrity is fundamental to ethics.")


add_question(170,"Ethics","Medium",
"Ethical choices balance:",
[
"Professional duties and client interests",
"Only profit",
"Only sales",
"Only convenience"
],
0,
"Ethics requires balanced judgement.")


add_question(171,"Competence","Easy",
"Competent advisors have:",
[
"Knowledge and skills",
"Only sales ability",
"No training",
"Limited information"
],
0,
"Competence requires ability and knowledge.")


add_question(172,"Competence","Medium",
"Continuing education supports:",
[
"Professional improvement",
"Guaranteed returns",
"Removing duties",
"Avoiding rules"
],
0,
"Education maintains competence.")


add_question(173,"Client Relationships","Easy",
"Fair treatment means:",
[
"Respecting clients",
"Using pressure",
"Hiding information",
"Ignoring concerns"
],
0,
"Clients should be treated fairly.")


add_question(174,"Client Relationships","Medium",
"Client trust is damaged by:",
[
"Dishonesty",
"Transparency",
"Clear advice",
"Good records"
],
0,
"Dishonesty harms trust.")


add_question(175,"Professional Standards","Medium",
"A professional advisor should maintain:",
[
"Ethical standards",
"Hidden practices",
"False promises",
"Poor records"
],
0,
"Professional standards guide behaviour.")



add_question(176,"Professional Conduct","Easy",
"An advisor's behaviour should reflect:",
[
"Integrity and professionalism",
"Personal gain",
"Pressure selling",
"Hidden information"
],
0,
"Professional conduct requires integrity.")


add_question(177,"Professional Conduct","Medium",
"Professional obligations include:",
[
"Acting honestly and fairly",
"Ignoring client concerns",
"Hiding conflicts",
"Making guarantees"
],
0,
"Advisors must act fairly.")


add_question(178,"Client Needs","Easy",
"Client information is used to:",
[
"Provide suitable advice",
"Increase commissions",
"Create pressure",
"Ignore objectives"
],
0,
"Information helps determine suitability.")


add_question(179,"Client Needs","Medium",
"Recommendations should be based on:",
[
"Client goals and circumstances",
"Advisor preference",
"Sales targets",
"Product popularity"
],
0,
"Recommendations should fit clients.")


add_question(180,"Disclosure","Easy",
"Important information should be:",
[
"Disclosed to clients",
"Hidden",
"Delayed",
"Ignored"
],
0,
"Clients need important information.")


add_question(181,"Disclosure","Medium",
"Proper disclosure supports:",
[
"Informed decisions",
"Guaranteed results",
"Reduced responsibility",
"Hidden conflicts"
],
0,
"Disclosure allows informed choices.")


add_question(182,"Compliance","Easy",
"An advisor should follow:",
[
"Applicable laws and regulations",
"Personal shortcuts",
"Market rumours",
"Sales pressure"
],
0,
"Rules guide professional conduct.")


add_question(183,"Compliance","Medium",
"Compliance failures may:",
[
"Lead to consequences",
"Guarantee success",
"Improve reputation",
"Remove duties"
],
0,
"Failure to comply may have penalties.")


add_question(184,"Privacy","Easy",
"Confidential information should be:",
[
"Protected",
"Published",
"Sold",
"Ignored"
],
0,
"Privacy requires protection.")


add_question(185,"Privacy","Medium",
"Privacy protection builds:",
[
"Client trust",
"Confusion",
"Pressure",
"Conflict"
],
0,
"Protecting information builds trust.")


add_question(186,"Risk","Easy",
"Explaining risk is part of:",
[
"Responsible advice",
"Misleading advice",
"Poor communication",
"Hidden practices"
],
0,
"Responsible advice includes risk explanation.")


add_question(187,"Risk","Medium",
"Clients should understand:",
[
"Risks before decisions",
"Only benefits",
"Guaranteed outcomes",
"Only fees"
],
0,
"Risk understanding supports decisions.")


add_question(188,"Suitability","Easy",
"Suitable recommendations:",
[
"Match client needs",
"Maximize commissions",
"Ignore goals",
"Follow trends"
],
0,
"Suitability means matching needs.")


add_question(189,"Suitability","Medium",
"An advisor should avoid:",
[
"Unsuitable recommendations",
"Client reviews",
"Clear explanations",
"Documentation"
],
0,
"Unsuitable advice can harm clients.")


add_question(190,"Documentation","Easy",
"Records should show:",
[
"Advice provided",
"Only sales",
"Only fees",
"Only signatures"
],
0,
"Records document the advice process.")


add_question(191,"Documentation","Medium",
"Good documentation demonstrates:",
[
"Professional responsibility",
"Hidden actions",
"Poor advice",
"Misleading conduct"
],
0,
"Records support accountability.")


add_question(192,"Communication","Easy",
"An advisor should:",
[
"Explain clearly",
"Hide information",
"Guarantee results",
"Ignore questions"
],
0,
"Clear explanations are required.")


add_question(193,"Communication","Medium",
"Effective communication includes:",
[
"Listening and explaining",
"Pressure tactics",
"Hidden details",
"False promises"
],
0,
"Communication requires understanding.")


add_question(194,"Ethics","Easy",
"Ethical advice requires:",
[
"Honesty",
"Deception",
"Bias",
"Negligence"
],
0,
"Honesty is an ethical requirement.")


add_question(195,"Ethics","Medium",
"Ethical behaviour protects:",
[
"Clients and public confidence",
"Only sales",
"Only profits",
"Only companies"
],
0,
"Ethics protects trust.")


add_question(196,"Competence","Easy",
"An advisor should maintain:",
[
"Professional knowledge",
"Outdated skills",
"Limited understanding",
"No training"
],
0,
"Knowledge must be maintained.")


add_question(197,"Competence","Medium",
"Competence improves through:",
[
"Education and experience",
"Guessing",
"Sales pressure",
"Ignoring changes"
],
0,
"Learning improves competence.")


add_question(198,"Client Relationships","Easy",
"Strong relationships require:",
[
"Trust and respect",
"Pressure",
"Hidden information",
"False promises"
],
0,
"Trust supports relationships.")


add_question(199,"Client Relationships","Medium",
"Client loyalty is supported by:",
[
"Ethical service",
"Misleading advice",
"Hidden fees",
"Poor communication"
],
0,
"Ethical service builds loyalty.")


add_question(200,"Ethics","Medium",
"The foundation of ethical advising is:",
[
"Integrity and client focus",
"Maximum sales",
"Personal benefit",
"Hidden information"
],
0,
"Ethical advising requires integrity.")



add_question(126,"Professional Conduct","Easy",
"An advisor should always:",
["Act honestly","Hide information","Promise results","Ignore rules"],
0,
"Honesty is a core professional duty.")

add_question(127,"Professional Conduct","Medium",
"Professional responsibility includes:",
["Following ethical standards","Maximizing sales only","Avoiding documentation","Ignoring concerns"],
0,
"Professionals follow ethical standards.")

add_question(128,"Client Needs","Easy",
"Client objectives should be:",
["Clearly identified","Ignored","Replaced with sales goals","Hidden"],
0,
"Understanding objectives supports advice.")

add_question(129,"Client Needs","Medium",
"A needs analysis helps determine:",
["Appropriate recommendations","Commission levels","Marketing plans","Sales rankings"],
0,
"Needs analysis supports suitability.")

add_question(130,"Risk","Easy",
"Explaining risk is part of:",
["Responsible advice","Sales pressure","Misleading communication","Hidden practices"],
0,
"Risk explanation is part of good advice.")

add_question(131,"Risk","Medium",
"Clients should understand:",
["Possible losses and uncertainty","Only possible gains","Guaranteed returns","Only fees"],
0,
"Clients need balanced risk information.")

add_question(132,"Compliance","Easy",
"An advisor must follow:",
["Applicable regulations","Personal preferences","Market rumours","Sales targets"],
0,
"Regulations guide professional conduct.")

add_question(133,"Compliance","Medium",
"Compliance supports:",
["Consumer protection","Hidden information","Poor documentation","Unfair practices"],
0,
"Compliance protects consumers.")

add_question(134,"Privacy","Easy",
"Personal information should be:",
["Protected","Shared publicly","Sold","Ignored"],
0,
"Privacy requires protection.")

add_question(135,"Privacy","Medium",
"Privacy breaches may:",
["Harm client trust","Improve relationships","Increase transparency","Reduce duties"],
0,
"Privacy breaches damage trust.")

add_question(136,"Disclosure","Easy",
"An advisor should disclose:",
["Important product facts","Only advantages","Only commissions","Nothing"],
0,
"Important facts must be disclosed.")

add_question(137,"Disclosure","Medium",
"Complete disclosure helps clients:",
["Evaluate choices","Avoid all risk","Guarantee outcomes","Remove contracts"],
0,
"Disclosure supports decisions.")

add_question(138,"Conflicts of Interest","Easy",
"Conflicts may arise from:",
["Personal interests","Client questions","Documentation","Education"],
0,
"Personal interests can create conflicts.")

add_question(139,"Conflicts of Interest","Medium",
"Conflict management requires:",
["Transparency","Secrecy","Ignoring issues","Removing clients"],
0,
"Transparency is required.")

add_question(140,"Documentation","Easy",
"Client files should contain:",
["Relevant information","False information","Missing details","Only signatures"],
0,
"Relevant records support advice.")

add_question(141,"Documentation","Medium",
"Good documentation helps:",
["Demonstrate proper advice","Hide decisions","Avoid accountability","Remove regulations"],
0,
"Records support accountability.")

add_question(142,"Communication","Easy",
"An advisor should explain information:",
["Clearly","Confusingly","Partially","Secretly"],
0,
"Clear communication is required.")

add_question(143,"Communication","Medium",
"Active listening helps advisors:",
["Understand client needs","Increase pressure","Avoid questions","Hide risks"],
0,
"Listening improves understanding.")

add_question(144,"Ethics","Easy",
"Ethical conduct requires:",
["Fairness","Deception","Pressure","Hidden conflicts"],
0,
"Fairness is an ethical principle.")

add_question(145,"Ethics","Medium",
"Ethical behaviour protects:",
["Clients and public confidence","Only sales","Only commissions","Only companies"],
0,
"Ethics supports trust.")

add_question(146,"Competence","Easy",
"An advisor should maintain:",
["Required knowledge","False confidence","Limited information","Outdated skills"],
0,
"Knowledge must be maintained.")

add_question(147,"Competence","Medium",
"Professional development helps:",
["Improve advice quality","Guarantee returns","Remove responsibility","Avoid rules"],
0,
"Learning improves competence.")

add_question(148,"Client Relationships","Easy",
"Respectful service includes:",
["Treating clients fairly","Using pressure","Ignoring concerns","Hiding information"],
0,
"Clients should be treated fairly.")

add_question(149,"Client Relationships","Medium",
"Client complaints should be:",
["Handled appropriately","Ignored","Hidden","Dismissed"],
0,
"Complaints require proper handling.")

add_question(150,"Professional Standards","Medium",
"Professional standards encourage:",
["Ethical and competent service","Misleading advice","Hidden practices","Poor records"],
0,
"Standards support quality service.")


with open(output,"w") as f:
    json.dump(questions,f,indent=2)

print("Generated questions:",len(questions))
