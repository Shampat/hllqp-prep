
import json

output = "app/src/main/assets/questions/annuities_questions.json"

questions = []

def add_question(qid, topic, difficulty, question, options, correct, explanation):
    questions.append({
        "id": qid,
        "moduleId": "annuities",
        "moduleName": "Annuities",
        "topic": topic,
        "difficulty": difficulty,
        "question": question,
        "options": options,
        "correctAnswer": correct,
        "explanation": explanation
    })


add_question(1,"Basics","Easy",
"What is an annuity?",
[
"A financial product that provides income payments",
"A type of home insurance",
"A bank loan",
"A government tax"
],
0,
"Annuities provide income payments according to contract terms.")

add_question(2,"Basics","Easy",
"The main purpose of an annuity is:",
[
"Provide income security",
"Guarantee stock profits",
"Remove all taxes",
"Replace all investments"
],
0,
"Annuities are designed to provide income.")

add_question(3,"Types of Annuities","Medium",
"An immediate annuity begins payments:",
[
"Shortly after purchase",
"Only after death",
"After many decades",
"Only during employment"
],
0,
"Immediate annuities begin income payments soon after purchase.")

add_question(4,"Types of Annuities","Medium",
"A deferred annuity begins payments:",
[
"At a future date",
"Immediately always",
"Only after a claim",
"Only after retirement ends"
],
0,
"Deferred annuities accumulate before income begins.")

add_question(5,"Contract Features","Easy",
"The annuitant is the person whose:",
[
"Life determines income payments",
"Investment account is managed",
"Taxes are calculated",
"Premium is paid by government"
],
0,
"The annuitant's life affects the payment period.")


add_question(6,"Basics","Easy",
"An annuity contract is issued by:",
[
"An insurance company",
"A stock exchange",
"A government office",
"A bank only"
],
0,
"Annuities are insurance products issued by insurers.")

add_question(7,"Basics","Medium",
"The owner of an annuity contract is called:",
[
"The policy owner",
"The beneficiary only",
"The advisor",
"The insurer"
],
0,
"The owner controls the contract rights.")

add_question(8,"Contract Features","Easy",
"The premium used to purchase an annuity is:",
[
"The amount invested into the contract",
"A tax payment",
"A claim payment",
"A commission only"
],
0,
"The premium purchases the annuity contract.")

add_question(9,"Contract Features","Medium",
"The beneficiary of an annuity receives:",
[
"Benefits according to contract terms",
"Guaranteed investment returns",
"Advisor payments",
"Government benefits"
],
0,
"Beneficiary benefits depend on contract provisions.")

add_question(10,"Types of Annuities","Easy",
"A life annuity provides income:",
[
"For the annuitant's lifetime",
"For one month only",
"Only during employment",
"Only after death"
],
0,
"Life annuities provide payments based on lifetime.")

add_question(11,"Types of Annuities","Medium",
"A joint life annuity covers:",
[
"More than one person's lifetime",
"Only one investment account",
"Only a beneficiary",
"Only a business"
],
0,
"Joint life annuities involve multiple lives.")

add_question(12,"Types of Annuities","Easy",
"A fixed annuity provides:",
[
"Specified payments according to contract",
"Unlimited market gains",
"No income",
"Only tax benefits"
],
0,
"Fixed annuities provide contract-based payments.")

add_question(13,"Types of Annuities","Medium",
"A variable annuity payment may depend on:",
[
"Investment performance",
"Only government rules",
"Advisor age",
"Contract colour"
],
0,
"Variable payments may change with investment results.")

add_question(14,"Income Payments","Easy",
"Annuity payments provide:",
[
"Regular income",
"Mortgage approval",
"Stock ownership",
"Tax refunds"
],
0,
"Annuities provide scheduled income payments.")

add_question(15,"Income Payments","Medium",
"The amount of annuity income depends on:",
[
"Contract terms and factors",
"Only advertising",
"Only commissions",
"Market rumours"
],
0,
"Income depends on several contract factors.")

add_question(16,"Contract Features","Easy",
"The accumulation period is:",
[
"Before income payments begin",
"After the contract ends",
"Only during claims",
"Only after death"
],
0,
"Deferred annuities have an accumulation period.")

add_question(17,"Contract Features","Medium",
"The payout period is:",
[
"When income payments are received",
"When premiums are paid",
"When investments are chosen",
"When taxes are filed"
],
0,
"The payout period is when income begins.")

add_question(18,"Retirement Planning","Easy",
"Annuities are commonly used for:",
[
"Retirement income planning",
"Buying property",
"Short-term loans",
"Tax avoidance"
],
0,
"Annuities can provide retirement income.")

add_question(19,"Retirement Planning","Medium",
"Annuities can help manage:",
[
"Longevity risk",
"Stock ownership",
"Employment risk",
"Mortgage risk"
],
0,
"Annuities help protect against outliving savings.")

add_question(20,"Contract Features","Easy",
"The annuity owner can:",
[
"Have rights under the contract",
"Control government policy",
"Guarantee profits",
"Remove all fees"
],
0,
"The owner has contractual rights.")

add_question(21,"Contract Features","Medium",
"Contract terms should be:",
[
"Reviewed carefully",
"Ignored",
"Changed randomly",
"Assumed"
],
0,
"Understanding the contract is important.")

add_question(22,"Beneficiaries","Easy",
"A beneficiary receives:",
[
"Contract benefits when applicable",
"All premiums immediately",
"Investment advice",
"Advisor compensation"
],
0,
"Beneficiary payments follow contract rules.")

add_question(23,"Beneficiaries","Medium",
"Beneficiary designations should be:",
[
"Reviewed periodically",
"Never changed",
"Hidden",
"Random"
],
0,
"Life changes may require updates.")

add_question(24,"Professional Conduct","Easy",
"An advisor should explain:",
[
"Benefits and limitations",
"Only advantages",
"Only sales information",
"Only fees"
],
0,
"Clients need complete information.")

add_question(25,"Professional Conduct","Medium",
"Suitable annuity advice considers:",
[
"Client needs and circumstances",
"Highest commission",
"Advisor preference",
"Market rumours"
],
0,
"Recommendations should be suitable.")



add_question(26,"Retirement Planning","Easy",
"Annuities provide protection against:",
[
"Outliving retirement savings",
"All investment losses",
"All taxes",
"All expenses"
],
0,
"Annuities can provide lifetime income protection.")

add_question(27,"Retirement Planning","Medium",
"Longevity risk means:",
[
"Risk of living longer than savings last",
"Risk of losing a job",
"Risk of changing investments",
"Risk of paying fees"
],
0,
"Longevity risk relates to retirement income lasting.")

add_question(28,"Types of Annuities","Easy",
"A deferred annuity has:",
[
"An accumulation period before income",
"Immediate payments only",
"No contract value",
"No owner"
],
0,
"Deferred annuities delay income payments.")

add_question(29,"Types of Annuities","Medium",
"An immediate annuity is useful when someone wants:",
[
"Income payments soon",
"Only investment growth",
"No payments",
"Only tax deductions"
],
0,
"Immediate annuities begin income quickly.")

add_question(30,"Income Payments","Easy",
"Annuity income frequency may be:",
[
"Monthly or according to contract",
"Only yearly always",
"Only once",
"Never"
],
0,
"Payment frequency is determined by contract.")

add_question(31,"Income Payments","Medium",
"Annuity payments are affected by:",
[
"Age, amount invested, and options selected",
"Only advertising",
"Only advisor choice",
"Only taxes"
],
0,
"Several factors determine income amounts.")

add_question(32,"Contract Features","Easy",
"A surrender value is:",
[
"Amount available if contract is ended early",
"Annual income payment",
"Tax refund",
"Commission payment"
],
0,
"Surrender value relates to early cancellation.")

add_question(33,"Contract Features","Medium",
"Surrendering an annuity may:",
[
"Reduce benefits and values",
"Increase guarantees always",
"Remove all rules",
"Create free income"
],
0,
"Ending contracts early may have consequences.")

add_question(34,"Contract Features","Easy",
"A contract guarantee is:",
[
"A promise stated in the contract",
"A market prediction",
"A sales opinion",
"A tax rule"
],
0,
"Guarantees are based on contract terms.")

add_question(35,"Contract Features","Medium",
"Guarantees should be explained with:",
[
"Applicable conditions",
"Only potential returns",
"Only fees",
"Market rumours"
],
0,
"Conditions determine guarantees.")

add_question(36,"Fees","Easy",
"An annuity may include:",
[
"Contract charges and fees",
"No costs ever",
"Only taxes",
"Only bonuses"
],
0,
"Contracts may contain various charges.")

add_question(37,"Fees","Medium",
"Clients should understand:",
[
"All applicable charges",
"Only income amount",
"Only market changes",
"Only advertising"
],
0,
"Fee understanding supports informed choices.")

add_question(38,"Tax Features","Easy",
"Annuity taxation depends on:",
[
"Applicable tax rules",
"Advisor preference",
"Market colour",
"Contract name"
],
0,
"Tax treatment follows legislation.")

add_question(39,"Tax Features","Medium",
"Tax questions may require:",
[
"Professional tax advice",
"Market prediction",
"Advertising review",
"No information"
],
0,
"Tax matters may require specialists.")

add_question(40,"Professional Conduct","Easy",
"An advisor should provide:",
[
"Accurate information",
"Guaranteed profits",
"Hidden details",
"False promises"
],
0,
"Accurate information is required.")

add_question(41,"Professional Conduct","Medium",
"Suitability means:",
[
"Recommendation matches client needs",
"Highest commission product",
"Most expensive option",
"Fastest sale"
],
0,
"Advice should fit client circumstances.")

add_question(42,"Professional Conduct","Easy",
"Client objectives should be:",
[
"Identified before recommending products",
"Ignored",
"Changed by advisor",
"Hidden"
],
0,
"Understanding objectives supports suitable advice.")

add_question(43,"Basics","Medium",
"An annuity differs from a regular investment because:",
[
"It provides contractual income features",
"It has no contract",
"It has no owner",
"It guarantees all profits"
],
0,
"Annuities are insurance contracts with income features.")

add_question(44,"Basics","Easy",
"The annuitant is important because:",
[
"Income may depend on their life",
"They manage the insurer",
"They set tax laws",
"They control markets"
],
0,
"The annuitant's life affects payments.")

add_question(45,"Basics","Medium",
"The owner and annuitant:",
[
"May be different people",
"Must always be identical",
"Cannot exist together",
"Are always beneficiaries"
],
0,
"Ownership and annuitant roles can differ.")

add_question(46,"Beneficiaries","Easy",
"Beneficiary payments depend on:",
[
"Contract provisions",
"Market rumours",
"Advisor choice",
"Advertising"
],
0,
"Contract terms determine benefits.")

add_question(47,"Beneficiaries","Medium",
"Updating beneficiaries may be needed after:",
[
"Major life events",
"Every payment",
"Every market change",
"Every fee"
],
0,
"Life changes may require updates.")

add_question(48,"Retirement Planning","Easy",
"Annuities may provide:",
[
"Predictable retirement income",
"Guaranteed stock prices",
"No contract",
"Free insurance"
],
0,
"Income predictability is a key feature.")

add_question(49,"Retirement Planning","Medium",
"Retirement income planning considers:",
[
"Client goals and financial situation",
"Only age",
"Only fees",
"Only markets"
],
0,
"Planning considers multiple factors.")

add_question(50,"Basics","Medium",
"The primary purpose of an annuity is:",
[
"Provide income based on contract terms",
"Eliminate all expenses",
"Guarantee market growth",
"Replace every investment"
],
0,
"Annuities are designed to provide income.")



add_question(51,"Contract Features","Easy",
"The contract owner is responsible for:",
[
"Understanding contract rights and features",
"Controlling the insurer",
"Setting tax laws",
"Guaranteeing returns"
],
0,
"The owner should understand contract features.")

add_question(52,"Contract Features","Medium",
"A contract review helps:",
[
"Confirm the contract still meets needs",
"Guarantee profits",
"Remove all risks",
"Change legislation"
],
0,
"Regular reviews support suitability.")

add_question(53,"Income Payments","Easy",
"Annuity income is paid:",
[
"According to contract terms",
"Only when markets rise",
"Only after claims",
"Only during employment"
],
0,
"Payments follow contract provisions.")

add_question(54,"Income Payments","Medium",
"Payment options may include:",
[
"Different income arrangements",
"Only one option always",
"No income",
"Only refunds"
],
0,
"Contracts may offer various payment options.")

add_question(55,"Types of Annuities","Easy",
"A life annuity is based on:",
[
"The annuitant's lifetime",
"The advisor's lifetime",
"Market prices",
"Government rules"
],
0,
"Life annuities depend on lifetime.")

add_question(56,"Types of Annuities","Medium",
"A term certain annuity provides payments:",
[
"For a specified period",
"Only forever",
"Only one day",
"Without a contract"
],
0,
"Term certain payments last a defined period.")

add_question(57,"Types of Annuities","Easy",
"A joint life annuity may cover:",
[
"Two individuals",
"Only an advisor",
"Only a beneficiary",
"Only a company"
],
0,
"Joint life covers more than one person.")

add_question(58,"Retirement Planning","Medium",
"Annuities are often used to create:",
[
"Retirement income streams",
"Market predictions",
"Tax refunds",
"Loan approvals"
],
0,
"Income streams support retirement planning.")

add_question(59,"Risk","Easy",
"An annuity can reduce:",
[
"Longevity risk",
"All investment risk",
"All expenses",
"All taxes"
],
0,
"Annuities address longevity risk.")

add_question(60,"Risk","Medium",
"Longevity risk increases when:",
[
"People live longer than expected",
"Markets increase",
"Fees decrease",
"Contracts change"
],
0,
"Living longer creates retirement income challenges.")

add_question(61,"Fees","Easy",
"Fees should be:",
[
"Disclosed to clients",
"Hidden",
"Ignored",
"Estimated randomly"
],
0,
"Fee disclosure is required.")

add_question(62,"Fees","Medium",
"Understanding fees helps clients:",
[
"Compare products properly",
"Guarantee returns",
"Remove contracts",
"Avoid income"
],
0,
"Clients need fee information.")

add_question(63,"Tax Features","Easy",
"Tax treatment may depend on:",
[
"Account type and legislation",
"Advisor preference",
"Market direction",
"Beneficiary choice"
],
0,
"Tax treatment follows applicable rules.")

add_question(64,"Tax Features","Medium",
"Clients should consider taxes when:",
[
"Planning retirement income",
"Ignoring contracts",
"Selecting colours",
"Choosing advisors"
],
0,
"Taxes can affect retirement planning.")

add_question(65,"Investment Features","Easy",
"An annuity may provide:",
[
"Income in exchange for a premium",
"Guaranteed market growth",
"No contract",
"Free investment"
],
0,
"Premiums fund annuity income.")

add_question(66,"Investment Features","Medium",
"The amount of income may depend on:",
[
"Interest rates and contract factors",
"Advisor salary",
"Government elections",
"Advertising"
],
0,
"Several factors influence payments.")

add_question(67,"Professional Conduct","Easy",
"An advisor should explain:",
[
"Product risks and benefits",
"Only benefits",
"Only commissions",
"Only sales goals"
],
0,
"Balanced explanations are required.")

add_question(68,"Professional Conduct","Medium",
"Misrepresentation means:",
[
"Providing false or misleading information",
"Explaining products",
"Documenting advice",
"Reviewing needs"
],
0,
"Misleading information is unacceptable.")

add_question(69,"Professional Conduct","Easy",
"Client information should be:",
[
"Handled appropriately",
"Shared publicly",
"Ignored",
"Destroyed immediately"
],
0,
"Client information requires proper handling.")

add_question(70,"Professional Conduct","Medium",
"Documentation should include:",
[
"Reasons for recommendations",
"Only product names",
"Only fees",
"Only signatures"
],
0,
"Documentation supports compliance.")

add_question(71,"Basics","Easy",
"An annuity combines:",
[
"Insurance contract features and income payments",
"Only stocks",
"Only loans",
"Only taxes"
],
0,
"Annuities are insurance-based products.")

add_question(72,"Basics","Medium",
"The insurer's obligation is based on:",
[
"Contract terms",
"Market rumours",
"Advisor opinions",
"Advertising"
],
0,
"Contract terms define obligations.")

add_question(73,"Contract Features","Easy",
"A premium is:",
[
"Money paid to purchase the annuity",
"A benefit payment",
"A tax penalty",
"A commission"
],
0,
"Premiums purchase the contract.")

add_question(74,"Contract Features","Medium",
"The owner should review:",
[
"Benefits, costs, and conditions",
"Only returns",
"Only advertisements",
"Only fees"
],
0,
"Complete review helps understanding.")

add_question(75,"Retirement Planning","Medium",
"Annuities are suitable when a client wants:",
[
"Reliable income payments",
"Guaranteed market performance",
"No contract",
"Only short-term gains"
],
0,
"Annuities are designed for income needs.")



add_question(76,"Income Payments","Easy",
"Annuity income payments are:",
[
"Specified by the contract",
"Always identical for every person",
"Based only on advertising",
"Controlled by markets only"
],
0,
"Payments depend on contract terms.")

add_question(77,"Income Payments","Medium",
"The income amount may be affected by:",
[
"Age and amount invested",
"Advisor preference",
"Office location",
"Advertising"
],
0,
"Several factors determine income.")

add_question(78,"Types of Annuities","Easy",
"A deferred annuity allows:",
[
"Income to begin later",
"Only immediate payments",
"No accumulation",
"No contract"
],
0,
"Deferred annuities postpone income.")

add_question(79,"Types of Annuities","Medium",
"The accumulation phase is when:",
[
"Money grows before income starts",
"Income payments are made",
"Claims are processed",
"Benefits end"
],
0,
"Accumulation occurs before payout.")

add_question(80,"Types of Annuities","Easy",
"The payout phase is when:",
[
"Income payments begin",
"Premiums are first paid",
"Investments are selected",
"Taxes are calculated"
],
0,
"Payout is the income stage.")

add_question(81,"Contract Features","Easy",
"A contract owner may:",
[
"Name beneficiaries",
"Control government rules",
"Guarantee markets",
"Remove legislation"
],
0,
"Owners may have contract rights such as naming beneficiaries.")

add_question(82,"Contract Features","Medium",
"Changing contract details may require:",
[
"Following contract procedures",
"Only verbal approval",
"Market approval",
"No documentation"
],
0,
"Changes must follow contract rules.")

add_question(83,"Beneficiaries","Easy",
"A beneficiary designation identifies:",
[
"Who receives benefits",
"Who sells the product",
"Who manages investments",
"Who sets taxes"
],
0,
"Beneficiaries receive contract benefits.")

add_question(84,"Beneficiaries","Medium",
"Beneficiary choices should consider:",
[
"Personal circumstances and goals",
"Market predictions",
"Advisor income",
"Advertising"
],
0,
"Choices should reflect client intentions.")

add_question(85,"Retirement Planning","Easy",
"Annuities can provide:",
[
"Income security in retirement",
"Guaranteed stock returns",
"Tax elimination",
"Debt repayment"
],
0,
"Income security is a common purpose.")

add_question(86,"Retirement Planning","Medium",
"Retirement planning should consider:",
[
"Income needs and expenses",
"Only age",
"Only investments",
"Only fees"
],
0,
"Complete planning considers financial needs.")

add_question(87,"Risk","Easy",
"Annuities may help manage:",
[
"Income uncertainty",
"All financial risks",
"All taxes",
"All market changes"
],
0,
"They can reduce uncertainty about income.")

add_question(88,"Risk","Medium",
"A client should understand:",
[
"Risks before purchasing",
"Only benefits",
"Only returns",
"Only guarantees"
],
0,
"Understanding risks supports informed decisions.")

add_question(89,"Fees","Easy",
"Charges in an annuity should be:",
[
"Explained clearly",
"Hidden",
"Ignored",
"Removed automatically"
],
0,
"Clear explanation of charges is important.")

add_question(90,"Fees","Medium",
"Clients compare annuities by considering:",
[
"Benefits, features, and costs",
"Only commissions",
"Only advertisements",
"Only payment dates"
],
0,
"Comparison requires complete information.")

add_question(91,"Professional Conduct","Easy",
"An advisor should recommend products based on:",
[
"Client suitability",
"Highest commission",
"Personal preference",
"Sales targets"
],
0,
"Recommendations must suit the client.")

add_question(92,"Professional Conduct","Medium",
"Good advice requires:",
[
"Understanding client circumstances",
"Guaranteeing results",
"Ignoring risks",
"Hiding costs"
],
0,
"Advice should be based on client needs.")

add_question(93,"Tax Features","Easy",
"Tax treatment of annuities depends on:",
[
"Applicable tax rules",
"Market colour",
"Advisor choice",
"Beneficiary choice"
],
0,
"Tax rules determine treatment.")

add_question(94,"Tax Features","Medium",
"Clients should seek tax advice when:",
[
"Tax issues are complex",
"They want predictions",
"They want guarantees",
"They avoid contracts"
],
0,
"Complex tax matters may require professionals.")

add_question(95,"Basics","Easy",
"An annuity is primarily designed for:",
[
"Income generation",
"Home ownership",
"Business loans",
"Stock trading"
],
0,
"Annuities provide income.")

add_question(96,"Basics","Medium",
"The insurer promises benefits according to:",
[
"The annuity contract",
"Market rumours",
"Advisor opinion",
"Advertising"
],
0,
"Contract terms define benefits.")

add_question(97,"Investment Features","Easy",
"An annuity premium represents:",
[
"The amount used to buy the contract",
"A tax payment",
"A claim",
"A refund"
],
0,
"Premiums purchase the annuity.")

add_question(98,"Investment Features","Medium",
"Investment-linked annuities may have:",
[
"Payments affected by investment performance",
"Fixed government returns",
"No risks",
"No contract"
],
0,
"Some annuities are linked to investments.")

add_question(99,"Contract Features","Easy",
"Before buying an annuity, a client should:",
[
"Review contract details",
"Ignore conditions",
"Assume guarantees",
"Avoid questions"
],
0,
"Reviewing details helps informed decisions.")

add_question(100,"Basics","Medium",
"The main benefit of an annuity is:",
[
"Providing scheduled income payments",
"Removing every financial risk",
"Guaranteeing market gains",
"Eliminating taxes"
],
0,
"Annuities provide structured income.")



add_question(101,"Basics","Easy",
"An annuity is a type of:",
[
"Insurance contract",
"Credit card",
"Mortgage",
"Government program"
],
0,
"Annuities are insurance contracts.")

add_question(102,"Basics","Medium",
"The purpose of an annuity contract is to:",
[
"Provide income according to terms",
"Guarantee all investments",
"Remove all expenses",
"Replace every financial product"
],
0,
"Annuities provide contractual income.")

add_question(103,"Contract Features","Easy",
"The annuity contract describes:",
[
"Rights and obligations",
"Market predictions",
"Government policy",
"Advisor goals"
],
0,
"Contracts define responsibilities and benefits.")

add_question(104,"Contract Features","Medium",
"Contract terms should be explained:",
[
"Before purchase",
"Only after claims",
"Never",
"Only during retirement"
],
0,
"Clients need understanding before purchasing.")

add_question(105,"Income Payments","Easy",
"Income payments may continue:",
[
"According to selected option",
"Only one month",
"Only during work",
"Only before purchase"
],
0,
"Payment duration depends on contract choice.")

add_question(106,"Income Payments","Medium",
"A life annuity generally provides:",
[
"Income for life",
"Income for one year",
"No income",
"Only refunds"
],
0,
"Life annuities provide lifetime income.")

add_question(107,"Types of Annuities","Easy",
"A fixed annuity generally provides:",
[
"Known payment features",
"Unlimited returns",
"No contract",
"Only market losses"
],
0,
"Fixed annuities have defined payment features.")

add_question(108,"Types of Annuities","Medium",
"A variable annuity may have payments based on:",
[
"Investment performance",
"Government decisions",
"Advisor income",
"Contract colour"
],
0,
"Variable payments can depend on investments.")

add_question(109,"Retirement Planning","Easy",
"Annuities can help provide:",
[
"Retirement income",
"Employment income",
"Business ownership",
"Tax refunds"
],
0,
"Annuities are commonly used for retirement income.")

add_question(110,"Retirement Planning","Medium",
"A retirement income strategy should consider:",
[
"Client goals and resources",
"Only product sales",
"Only fees",
"Only markets"
],
0,
"Planning requires understanding the client.")

add_question(111,"Risk","Easy",
"Longevity risk refers to:",
[
"Living longer than expected savings",
"Investment growth",
"Changing jobs",
"Paying premiums"
],
0,
"Longevity risk involves outliving savings.")

add_question(112,"Risk","Medium",
"Annuities can reduce longevity risk by:",
[
"Providing income payments",
"Removing all taxes",
"Guaranteeing markets",
"Removing contracts"
],
0,
"Income payments may continue for life.")

add_question(113,"Fees","Easy",
"Clients should receive information about:",
[
"Fees and charges",
"Only profits",
"Only guarantees",
"Only investments"
],
0,
"Fee disclosure supports transparency.")

add_question(114,"Fees","Medium",
"Understanding fees helps clients:",
[
"Make informed decisions",
"Guarantee returns",
"Remove risk",
"Avoid contracts"
],
0,
"Costs are part of product evaluation.")

add_question(115,"Tax Features","Easy",
"Tax rules are determined by:",
[
"Legislation",
"Advisor preference",
"Market movement",
"Beneficiary choice"
],
0,
"Tax treatment follows laws.")

add_question(116,"Tax Features","Medium",
"Tax treatment should be:",
[
"Explained accurately",
"Guaranteed",
"Ignored",
"Estimated randomly"
],
0,
"Accurate explanations are required.")

add_question(117,"Professional Conduct","Easy",
"An advisor should:",
[
"Act honestly",
"Hide information",
"Promise returns",
"Ignore risks"
],
0,
"Honesty is a professional responsibility.")

add_question(118,"Professional Conduct","Medium",
"Suitable advice considers:",
[
"Client circumstances",
"Advisor commission",
"Sales targets",
"Market rumours"
],
0,
"Suitability depends on client needs.")

add_question(119,"Beneficiaries","Easy",
"Beneficiaries receive:",
[
"Benefits according to contract",
"Advisor payments",
"Market gains",
"Tax refunds"
],
0,
"Beneficiary benefits follow contract terms.")

add_question(120,"Beneficiaries","Medium",
"Beneficiary designations should be:",
[
"Reviewed regularly",
"Ignored",
"Changed randomly",
"Hidden"
],
0,
"Regular reviews help keep information current.")

add_question(121,"Contract Features","Easy",
"The owner of an annuity has:",
[
"Contract rights",
"Control of markets",
"Control of laws",
"Guaranteed profits"
],
0,
"The owner has rights under the contract.")

add_question(122,"Contract Features","Medium",
"Ending an annuity early may:",
[
"Have financial consequences",
"Increase income automatically",
"Remove all fees",
"Guarantee returns"
],
0,
"Early termination may affect values.")

add_question(123,"Investment Features","Easy",
"Investment choices should match:",
[
"Client objectives",
"Advisor preference",
"Market rumours",
"Advertising"
],
0,
"Suitability is important.")

add_question(124,"Investment Features","Medium",
"Investment performance does not:",
[
"Guarantee future results",
"Change values",
"Affect some products",
"Need review"
],
0,
"Past performance is not guaranteed.")

add_question(125,"Basics","Medium",
"Annuities should be selected based on:",
[
"Client needs and goals",
"Highest commission",
"Random choice",
"Advertising"
],
0,
"Product selection should be suitable.")



add_question(126,"Income Payments","Easy",
"An annuity payment schedule is:",
[
"Defined by the contract",
"Chosen by the market",
"Set by advertising",
"Changed daily"
],
0,
"Payment schedules are stated in the contract.")

add_question(127,"Income Payments","Medium",
"Payment options should be selected based on:",
[
"Client income needs",
"Advisor preference",
"Market rumours",
"Commission amount"
],
0,
"Options should match client needs.")

add_question(128,"Types of Annuities","Easy",
"A single life annuity covers:",
[
"One person's lifetime",
"Multiple companies",
"Only beneficiaries",
"Only investments"
],
0,
"A single life annuity is based on one life.")

add_question(129,"Types of Annuities","Medium",
"A joint life annuity provides income based on:",
[
"Two or more lives",
"Only market value",
"Only fees",
"Only taxes"
],
0,
"Joint life annuities involve multiple people.")

add_question(130,"Contract Features","Easy",
"A contract value represents:",
[
"Value within the annuity contract",
"Advisor income",
"Government funding",
"Tax payment"
],
0,
"Contract value relates to the annuity.")

add_question(131,"Contract Features","Medium",
"Contract changes should be:",
[
"Documented properly",
"Made secretly",
"Ignored",
"Based on rumours"
],
0,
"Proper procedures are required.")

add_question(132,"Retirement Planning","Easy",
"Annuities can provide:",
[
"Predictable retirement income",
"Guaranteed stock prices",
"No expenses",
"Employment benefits"
],
0,
"Income predictability is a key feature.")

add_question(133,"Retirement Planning","Medium",
"A retirement plan should include:",
[
"Income needs and objectives",
"Only investments",
"Only age",
"Only taxes"
],
0,
"Planning considers many factors.")

add_question(134,"Risk","Easy",
"Investment risk means:",
[
"Possibility of losing value",
"Guaranteed loss",
"Guaranteed growth",
"No changes"
],
0,
"Risk involves possible value changes.")

add_question(135,"Risk","Medium",
"Clients should understand:",
[
"Possible risks before purchase",
"Only benefits",
"Only payments",
"Only fees"
],
0,
"Risk awareness supports decisions.")

add_question(136,"Fees","Easy",
"Fees reduce:",
[
"Net investment value",
"Contract ownership",
"Beneficiary rights",
"Tax laws"
],
0,
"Fees can affect net results.")

add_question(137,"Fees","Medium",
"Comparing annuities requires reviewing:",
[
"Costs and benefits",
"Only fees",
"Only returns",
"Only advertising"
],
0,
"Both costs and benefits matter.")

add_question(138,"Tax Features","Easy",
"Tax rules may:",
[
"Change over time",
"Never change",
"Depend on advisors",
"Depend on markets"
],
0,
"Tax laws can change.")

add_question(139,"Tax Features","Medium",
"Tax planning should consider:",
[
"Current legislation",
"Market rumours",
"Sales goals",
"Advertising"
],
0,
"Tax planning uses current rules.")

add_question(140,"Professional Conduct","Easy",
"Advisors should avoid:",
[
"Misleading statements",
"Clear explanations",
"Documentation",
"Client reviews"
],
0,
"Misleading information is prohibited.")

add_question(141,"Professional Conduct","Medium",
"Professional advice requires:",
[
"Knowledge and honesty",
"Guaranteed results",
"Hidden costs",
"Random choices"
],
0,
"Professional standards require honesty.")

add_question(142,"Beneficiaries","Easy",
"A beneficiary may receive:",
[
"Contract benefits",
"Advisor fees",
"Market control",
"Tax authority"
],
0,
"Beneficiaries receive benefits according to terms.")

add_question(143,"Beneficiaries","Medium",
"Beneficiary information should be:",
[
"Kept current",
"Ignored",
"Hidden",
"Changed randomly"
],
0,
"Updates may be needed after life events.")

add_question(144,"Basics","Easy",
"Annuities are designed mainly for:",
[
"Income generation",
"Property purchase",
"Business loans",
"Tax avoidance"
],
0,
"Income generation is the main purpose.")

add_question(145,"Basics","Medium",
"The insurer's promise is based on:",
[
"Contract obligations",
"Market predictions",
"Advertising",
"Advisor opinion"
],
0,
"Contracts define insurer obligations.")

add_question(146,"Investment Features","Easy",
"Investment performance can affect:",
[
"Some annuity values",
"Tax laws",
"Beneficiary names",
"Advisor license"
],
0,
"Some products are investment-linked.")

add_question(147,"Investment Features","Medium",
"Clients should review investments:",
[
"Regularly",
"Never",
"Only after losses",
"Only before purchase"
],
0,
"Regular reviews support planning.")

add_question(148,"Contract Features","Easy",
"Reading the contract helps clients understand:",
[
"Features and limitations",
"Market predictions",
"Government rules",
"Advisor income"
],
0,
"Contracts explain features and limitations.")

add_question(149,"Contract Features","Medium",
"Important contract information includes:",
[
"Benefits, costs, and conditions",
"Only returns",
"Only fees",
"Only names"
],
0,
"Complete information supports understanding.")

add_question(150,"Retirement Planning","Medium",
"Annuities may be appropriate for clients seeking:",
[
"Reliable income",
"Guaranteed stock gains",
"No contracts",
"Unlimited returns"
],
0,
"Annuities provide structured income.")



add_question(151,"Income Payments","Easy",
"Annuity income is generally paid:",
[
"According to contract terms",
"According to stock prices",
"Only by advisors",
"Only by government"
],
0,
"Payments follow the annuity contract.")

add_question(152,"Income Payments","Medium",
"Income payment options may affect:",
[
"Amount and duration of payments",
"Only fees",
"Only taxes",
"Only ownership"
],
0,
"Options influence income features.")

add_question(153,"Types of Annuities","Easy",
"An immediate annuity is designed for:",
[
"Income beginning soon",
"Only long-term growth",
"No payments",
"Only investments"
],
0,
"Immediate annuities begin income shortly after purchase.")

add_question(154,"Types of Annuities","Medium",
"A deferred annuity may be suitable when:",
[
"Income is needed in the future",
"Income is needed immediately only",
"No contract is wanted",
"Markets are guaranteed"
],
0,
"Deferred annuities delay income.")

add_question(155,"Contract Features","Easy",
"The contract holder should know:",
[
"Contract features and obligations",
"Only investment returns",
"Only advertising",
"Only fees"
],
0,
"Understanding the contract is important.")

add_question(156,"Contract Features","Medium",
"Contract limitations are:",
[
"Important information",
"Unnecessary details",
"Always removed",
"Market predictions"
],
0,
"Limitations affect contract benefits.")

add_question(157,"Retirement Planning","Easy",
"Annuities can create:",
[
"A stream of income",
"A stock portfolio",
"A loan",
"A tax account"
],
0,
"Income streams are a common purpose.")

add_question(158,"Retirement Planning","Medium",
"A retirement income decision should consider:",
[
"Financial goals and circumstances",
"Only commissions",
"Only age",
"Only advertising"
],
0,
"Personal circumstances matter.")

add_question(159,"Risk","Easy",
"Guaranteed income may help manage:",
[
"Income uncertainty",
"All financial problems",
"All taxes",
"All investments"
],
0,
"Income guarantees may reduce uncertainty.")

add_question(160,"Risk","Medium",
"Clients should balance:",
[
"Risk and desired income",
"Only returns",
"Only fees",
"Only guarantees"
],
0,
"Planning requires balancing objectives.")

add_question(161,"Fees","Easy",
"Fee information should be:",
[
"Provided clearly",
"Hidden",
"Ignored",
"Estimated"
],
0,
"Transparency is important.")

add_question(162,"Fees","Medium",
"High fees may:",
[
"Reduce net returns",
"Guarantee income",
"Remove risk",
"Increase ownership"
],
0,
"Fees can affect results.")

add_question(163,"Tax Features","Easy",
"Tax treatment depends on:",
[
"Applicable rules",
"Advisor preference",
"Market changes",
"Beneficiary choice"
],
0,
"Tax rules determine treatment.")

add_question(164,"Tax Features","Medium",
"Tax advice should be:",
[
"Accurate and appropriate",
"Guaranteed",
"Based on rumours",
"Ignored"
],
0,
"Proper advice should be accurate.")

add_question(165,"Professional Conduct","Easy",
"Advisors should:",
[
"Explain products honestly",
"Promise profits",
"Hide risks",
"Ignore needs"
],
0,
"Honest explanations are required.")

add_question(166,"Professional Conduct","Medium",
"Client suitability requires:",
[
"Matching products to needs",
"Choosing highest commission",
"Ignoring objectives",
"Following rumours"
],
0,
"Suitability is client-focused.")

add_question(167,"Beneficiaries","Easy",
"Beneficiary choices should reflect:",
[
"Client wishes",
"Market conditions",
"Advisor income",
"Sales targets"
],
0,
"Clients choose based on intentions.")

add_question(168,"Beneficiaries","Medium",
"Beneficiaries may need updating after:",
[
"Major life changes",
"Market changes only",
"Every payment",
"Every fee"
],
0,
"Life events may require updates.")

add_question(169,"Basics","Easy",
"Annuities are:",
[
"Insurance products",
"Bank loans",
"Stocks only",
"Government plans"
],
0,
"Annuities are insurance contracts.")

add_question(170,"Basics","Medium",
"The value of an annuity depends on:",
[
"Contract terms and selected options",
"Advertising",
"Advisor preference",
"Random changes"
],
0,
"Contract features determine value.")

add_question(171,"Investment Features","Easy",
"Some annuities include:",
[
"Investment components",
"No investments",
"Only taxes",
"Only loans"
],
0,
"Some annuities include investment options.")

add_question(172,"Investment Features","Medium",
"Investment choices should be reviewed because:",
[
"Client needs may change",
"Markets never change",
"Contracts disappear",
"Fees stop"
],
0,
"Regular reviews help maintain suitability.")

add_question(173,"Contract Features","Easy",
"Annuity guarantees are:",
[
"Defined in the contract",
"Always unlimited",
"Market promises",
"Advisor promises"
],
0,
"Guarantees are contractual.")

add_question(174,"Contract Features","Medium",
"Before purchasing, clients should:",
[
"Understand terms and conditions",
"Ignore details",
"Assume guarantees",
"Avoid questions"
],
0,
"Understanding the contract is essential.")

add_question(175,"Retirement Planning","Medium",
"The main retirement benefit of an annuity is:",
[
"Regular income payments",
"Guaranteed market returns",
"No contract requirements",
"Tax elimination"
],
0,
"Annuities provide structured retirement income.")



add_question(176,"Basics","Easy",
"An annuity provides:",
[
"Income payments",
"Stock ownership",
"Mortgage protection",
"Tax refunds"
],
0,
"Annuities provide income.")

add_question(177,"Basics","Medium",
"The primary purpose of an annuity is:",
[
"Create income from a contract",
"Guarantee all investments",
"Remove all expenses",
"Replace all insurance"
],
0,
"Income creation is the main purpose.")

add_question(178,"Income Payments","Easy",
"An annuity payment is:",
[
"A scheduled income amount",
"A stock dividend",
"A tax payment",
"A loan repayment"
],
0,
"Payments are made according to contract terms.")

add_question(179,"Income Payments","Medium",
"Income payments can vary depending on:",
[
"Contract type and options",
"Advisor choice",
"Advertising",
"Government elections"
],
0,
"Contract features determine payments.")

add_question(180,"Types of Annuities","Easy",
"A deferred annuity delays:",
[
"Income payments",
"Contract ownership",
"Premium payment",
"Insurance coverage"
],
0,
"Deferred annuities postpone income.")

add_question(181,"Types of Annuities","Medium",
"An immediate annuity is useful for:",
[
"Immediate income needs",
"Only growth",
"No income",
"Only savings"
],
0,
"Immediate annuities provide income quickly.")

add_question(182,"Contract Features","Easy",
"The owner should understand:",
[
"Contract rights and responsibilities",
"Market predictions",
"Advisor goals",
"Advertising"
],
0,
"Owners need contract knowledge.")

add_question(183,"Contract Features","Medium",
"Contract review should include:",
[
"Benefits, costs, and conditions",
"Only payments",
"Only fees",
"Only returns"
],
0,
"Complete review is important.")

add_question(184,"Risk","Easy",
"Annuities may reduce:",
[
"Longevity risk",
"All risks",
"All taxes",
"All expenses"
],
0,
"They help manage longevity risk.")

add_question(185,"Risk","Medium",
"Risk tolerance helps determine:",
[
"Suitable product choices",
"Tax rates",
"Government policy",
"Contract wording"
],
0,
"Risk tolerance affects suitability.")

add_question(186,"Fees","Easy",
"Clients should know:",
[
"Fees charged",
"Only profits",
"Only benefits",
"Only guarantees"
],
0,
"Fee transparency is required.")

add_question(187,"Fees","Medium",
"Product comparisons should include:",
[
"Costs and features",
"Only commissions",
"Only returns",
"Only advertising"
],
0,
"Comparisons require complete information.")

add_question(188,"Tax Features","Easy",
"Tax rules may affect:",
[
"Annuity income",
"Market prices",
"Advisor licensing",
"Contract ownership"
],
0,
"Tax treatment can affect income.")

add_question(189,"Tax Features","Medium",
"Tax advice should be obtained from:",
[
"Qualified professionals when needed",
"Friends",
"Advertisements",
"Market reports"
],
0,
"Complex tax issues require expertise.")

add_question(190,"Professional Conduct","Easy",
"An advisor must:",
[
"Act professionally",
"Hide information",
"Promise returns",
"Ignore clients"
],
0,
"Professional conduct is required.")

add_question(191,"Professional Conduct","Medium",
"Good documentation records:",
[
"Advice and recommendations",
"Only commissions",
"Only fees",
"Only sales"
],
0,
"Documentation supports compliance.")

add_question(192,"Beneficiaries","Easy",
"Beneficiary information should be:",
[
"Accurate and current",
"Hidden",
"Ignored",
"Random"
],
0,
"Current information is important.")

add_question(193,"Beneficiaries","Medium",
"Beneficiary planning supports:",
[
"Transfer of benefits",
"Market growth",
"Tax avoidance",
"Fee removal"
],
0,
"Beneficiary planning supports transfer.")

add_question(194,"Retirement Planning","Easy",
"Annuities can support:",
[
"Retirement income needs",
"Home purchases",
"Business loans",
"Stock trading"
],
0,
"They are commonly used for retirement income.")

add_question(195,"Retirement Planning","Medium",
"A retirement plan should be:",
[
"Reviewed periodically",
"Ignored",
"Based only on age",
"Based only on markets"
],
0,
"Plans should be reviewed as circumstances change.")

add_question(196,"Investment Features","Easy",
"Investment performance may affect:",
[
"Some annuity values",
"Tax laws",
"Contract ownership",
"Beneficiary rights"
],
0,
"Some products are investment-linked.")

add_question(197,"Investment Features","Medium",
"Past investment performance:",
[
"Does not guarantee future results",
"Guarantees profits",
"Removes risk",
"Sets contract rules"
],
0,
"Past results do not guarantee future outcomes.")

add_question(198,"Contract Features","Easy",
"Guarantees are based on:",
[
"Contract terms",
"Market rumours",
"Advisor promises",
"Advertising"
],
0,
"Guarantees are contractual.")

add_question(199,"Professional Conduct","Medium",
"Suitable advice considers:",
[
"Client objectives and situation",
"Highest commission",
"Advisor preference",
"Market rumours"
],
0,
"Advice must suit the client.")

add_question(200,"Basics","Medium",
"The main purpose of annuities is:",
[
"Provide income security",
"Guarantee every investment",
"Remove all taxes",
"Replace all products"
],
0,
"Annuities provide income security.")


with open(output,"w") as f:
    json.dump(questions,f,indent=2)

print("Generated questions:",len(questions))
