
import json

output = "app/src/main/assets/questions/segregated_funds_questions.json"

questions = []

def add_question(qid, topic, difficulty, question, options, correct, explanation):
    questions.append({
        "id": qid,
        "moduleId": "segregated",
        "moduleName": "Segregated Funds",
        "topic": topic,
        "difficulty": difficulty,
        "question": question,
        "options": options,
        "correctAnswer": correct,
        "explanation": explanation
    })

add_question(1,"Basics","Easy",
"What is a segregated fund?",
[
"A type of investment insurance product",
"A bank account only",
"A government pension plan",
"A regular savings account"
],
0,
"Segregated funds combine investment features with insurance protection.")

add_question(2,"Basics","Easy",
"Segregated funds are offered by:",
[
"Insurance companies",
"Only banks",
"Stock exchanges",
"Government agencies"
],
0,
"Segregated funds are insurance contracts offered by insurers.")

add_question(3,"Contract Features","Medium",
"A segregated fund contract includes:",
[
"Insurance guarantees and investment options",
"Only stock ownership",
"Only tax payments",
"No contractual terms"
],
0,
"Segregated funds provide investment choices with insurance features.")

add_question(4,"Guarantees","Medium",
"A maturity guarantee protects:",
[
"A portion of the investment value at maturity",
"All market gains forever",
"Only commissions",
"All withdrawals"
],
0,
"Maturity guarantees provide protection at the contract maturity date.")

add_question(5,"Guarantees","Medium",
"A death benefit guarantee provides protection when:",
[
"The contract holder dies",
"The market rises",
"A premium is missed",
"The investor changes funds"
],
0,
"Death benefit guarantees protect beneficiaries according to contract terms.")


add_question(6,"Investment Features","Easy",
"Segregated funds allow investors to:",
["Choose from investment options","Avoid all market risk","Guarantee profits","Remove all fees"],
0,
"Investors can select from available investment options.")

add_question(7,"Investment Features","Medium",
"The value of segregated funds is generally affected by:",
["Market performance","Only age","Only location","Government decisions"],
0,
"Investment values can change based on market performance.")

add_question(8,"Contract Features","Easy",
"The contract holder is the person who:",
["Owns the segregated fund contract","Manages the insurer","Sets government rules","Receives all claims automatically"],
0,
"The contract holder owns the insurance investment contract.")

add_question(9,"Contract Features","Medium",
"A segregated fund contract combines:",
["Investment and insurance features","Only banking services","Only tax benefits","Only savings"],
0,
"Segregated funds combine investment opportunities with guarantees.")

add_question(10,"Guarantees","Medium",
"A guarantee in a segregated fund is based on:",
["Contract terms","Market rumours","Advisor opinion","Stock predictions"],
0,
"Guarantees depend on the insurance contract.")

add_question(11,"Guarantees","Easy",
"The beneficiary receives:",
["Death benefit proceeds","Premium payments","Investment advice","Tax refunds"],
0,
"Beneficiaries receive benefits according to contract terms.")

add_question(12,"Fees","Easy",
"Segregated funds may include:",
["Management fees","No costs ever","Guaranteed profits","Free insurance"],
0,
"Investment products may have management fees.")

add_question(13,"Fees","Medium",
"Fees should be explained because:",
["They affect investment returns","They increase guarantees automatically","They remove risks","They replace contracts"],
0,
"Clients should understand product costs.")

add_question(14,"Professional Conduct","Medium",
"An advisor should explain:",
["Benefits, risks, and costs","Only advantages","Only guarantees","Only fees"],
0,
"Clients need complete information.")

add_question(15,"Professional Conduct","Easy",
"Suitability means recommending:",
["Products appropriate for client needs","The most expensive product","Any available product","Only popular products"],
0,
"Recommendations should match client circumstances.")

add_question(16,"Investment Features","Medium",
"Market value refers to:",
["Current investment value","Original premium only","Guaranteed amount only","Tax amount"],
0,
"Market value changes with investment performance.")

add_question(17,"Investment Features","Easy",
"Segregated funds provide access to:",
["Investment portfolios","Only chequing accounts","Mortgages","Government bonds only"],
0,
"Segregated funds offer investment choices.")

add_question(18,"Guarantees","Medium",
"Guarantees are valuable because they:",
["Provide protection against some losses","Guarantee unlimited profits","Remove all fees","Prevent all market changes"],
0,
"Guarantees provide protection under specified conditions.")

add_question(19,"Withdrawals","Medium",
"Withdrawals from segregated funds may:",
["Reduce guarantees","Increase guarantees automatically","Remove fees permanently","Create insurance coverage"],
0,
"Withdrawals may affect guaranteed values.")

add_question(20,"Withdrawals","Easy",
"Before withdrawing money, clients should consider:",
["Contract impact","Only market rumours","Only taxes","Only commissions"],
0,
"Withdrawals may affect contract benefits.")

add_question(21,"Basics","Easy",
"Segregated funds are considered:",
["Insurance investment products","Regular savings accounts","Government programs","Loans"],
0,
"They are insurance contracts with investment components.")

add_question(22,"Basics","Medium",
"The insurer provides:",
["Contractual guarantees","Stock market predictions","Tax advice only","Banking services"],
0,
"The insurer provides guarantees stated in the contract.")

add_question(23,"Beneficiaries","Easy",
"A beneficiary designation allows:",
["Payment to selected individuals after death","Guaranteed investment growth","Free withdrawals","Tax elimination"],
0,
"Beneficiaries receive contract benefits.")

add_question(24,"Beneficiaries","Medium",
"Beneficiary information should be:",
["Reviewed and updated when needed","Ignored forever","Shared publicly","Removed automatically"],
0,
"Keeping beneficiary information current is important.")

add_question(25,"Basics","Medium",
"The main purpose of segregated funds is:",
["Combine investment growth potential with insurance protection","Guarantee every investment","Avoid all fees","Replace all insurance"],
0,
"Segregated funds combine investment and insurance features.")



add_question(26,"Investment Features","Medium",
"Segregated funds are invested in:",
["Underlying investment funds","Only cash accounts","Government offices","Personal loans"],
0,
"Segregated funds invest in underlying funds selected by the investor.")

add_question(27,"Investment Features","Easy",
"The investment value of a segregated fund may:",
["Increase or decrease with markets","Never change","Only increase","Always stay guaranteed"],
0,
"Market performance affects investment value.")

add_question(28,"Contract Features","Medium",
"The contract maturity date is:",
["The date when maturity guarantees apply","The purchase date only","The withdrawal date","The tax date"],
0,
"Maturity guarantees apply at the contract maturity date.")

add_question(29,"Guarantees","Medium",
"Maturity guarantees are based on:",
["Specified contract conditions","Market predictions","Advisor promises","Government decisions"],
0,
"Guarantees are defined in the contract.")

add_question(30,"Guarantees","Easy",
"A death benefit guarantee protects:",
["Beneficiaries","The stock market","The advisor","The government"],
0,
"Death benefit guarantees provide protection to beneficiaries.")

add_question(31,"Fees","Medium",
"Management expense ratios affect:",
["Investment returns","Beneficiary choices","Contract ownership","Insurance claims"],
0,
"Fees reduce the net investment return.")

add_question(32,"Fees","Easy",
"Clients should understand fees because:",
["Costs affect returns","Fees guarantee profits","Fees remove risk","Fees create beneficiaries"],
0,
"Understanding costs helps clients make informed decisions.")

add_question(33,"Risk","Medium",
"Investment risk refers to:",
["Possibility that investment value changes","Guaranteed loss","Insurance fees only","Contract ownership"],
0,
"Investment values can fluctuate.")

add_question(34,"Risk","Easy",
"Segregated funds may reduce risk through:",
["Insurance guarantees","Higher fees only","No investments","Government payments"],
0,
"Guarantees can provide some protection.")

add_question(35,"Professional Conduct","Medium",
"An advisor must explain:",
["Risks and benefits","Only potential gains","Only guarantees","Only fees"],
0,
"Balanced disclosure is required.")

add_question(36,"Professional Conduct","Easy",
"Client information should be:",
["Kept confidential","Shared publicly","Sold to others","Ignored"],
0,
"Privacy is a professional responsibility.")

add_question(37,"Professional Conduct","Medium",
"A suitable recommendation considers:",
["Client objectives and risk tolerance","Commission only","Market rumours","Advisor preference"],
0,
"Suitability requires understanding the client.")

add_question(38,"Risk","Medium",
"Risk tolerance measures:",
["How much investment risk a client can accept","The amount of fees","The contract date","The beneficiary name"],
0,
"Risk tolerance helps determine suitable investments.")

add_question(39,"Investment Features","Easy",
"Asset allocation means:",
["How investments are divided among categories","The insurance premium","The beneficiary list","The contract owner"],
0,
"Asset allocation describes investment distribution.")

add_question(40,"Investment Features","Medium",
"Diversification helps:",
["Spread investment risk","Guarantee profits","Remove all losses","Avoid contracts"],
0,
"Diversification can reduce concentration risk.")

add_question(41,"Withdrawals","Medium",
"Early withdrawals may:",
["Affect guarantees","Increase guarantees automatically","Remove all fees","Create new coverage"],
0,
"Withdrawals can reduce guaranteed amounts.")

add_question(42,"Withdrawals","Easy",
"Clients should review withdrawal rules because:",
["Contract values may change","Withdrawals are always free","Guarantees always increase","Fees disappear"],
0,
"Withdrawal provisions affect contract benefits.")

add_question(43,"Beneficiaries","Medium",
"A beneficiary designation may provide:",
["Protection for estate planning goals","Guaranteed returns","No contract terms","Unlimited withdrawals"],
0,
"Beneficiary designations are useful estate planning tools.")

add_question(44,"Beneficiaries","Easy",
"Beneficiary information should be:",
["Accurate and current","Hidden from the owner","Ignored","Changed randomly"],
0,
"Current beneficiary information helps ensure proper payment.")

add_question(45,"Tax Features","Medium",
"Tax treatment of segregated funds depends on:",
["Applicable tax rules","Market performance only","Advisor choice","Investment colour"],
0,
"Tax treatment follows applicable laws.")

add_question(46,"Tax Features","Easy",
"Clients should seek tax advice when:",
["Tax issues are complex","Buying any product","Changing beneficiaries only","Reviewing markets"],
0,
"Professional tax advice may be appropriate.")

add_question(47,"Basics","Medium",
"A segregated fund contract is different from a mutual fund because it:",
["Includes insurance features","Has no investments","Cannot change value","Is only a bank product"],
0,
"Segregated funds include insurance guarantees.")

add_question(48,"Basics","Easy",
"Segregated funds are designed for:",
["Investors seeking investment and insurance features","Only borrowers","Only businesses","Only governments"],
0,
"They combine investment options with insurance protection.")

add_question(49,"Contract Features","Medium",
"Contract terms should be:",
["Reviewed carefully","Ignored","Changed without approval","Assumed"],
0,
"Understanding contract terms is important.")

add_question(50,"Professional Conduct","Medium",
"The best recommendation is based on:",
["Client needs and circumstances","Highest commission","Market rumours","Advisor convenience"],
0,
"Recommendations should be suitable for the client.")



add_question(51,"Contract Features","Easy",
"The policyholder of a segregated fund is the person who:",
["Owns the contract","Manages the stock market","Creates tax laws","Guarantees returns"],
0,
"The policyholder owns the insurance contract.")

add_question(52,"Contract Features","Medium",
"The contract holder can usually:",
["Make decisions about the contract","Change government rules","Control markets","Guarantee profits"],
0,
"The contract holder has rights under the contract.")

add_question(53,"Investment Features","Easy",
"Investment options allow clients to:",
["Select different funds","Avoid all risk","Remove insurance","Change laws"],
0,
"Clients may choose from available investment options.")

add_question(54,"Investment Features","Medium",
"Fund performance depends on:",
["Underlying investments","Beneficiary choices","Contract colour","Advisor location"],
0,
"Performance is linked to the investments held.")

add_question(55,"Risk","Easy",
"Market risk means:",
["Investment values can fluctuate","Benefits disappear always","Contracts end automatically","Fees stop"],
0,
"Market movements affect investment values.")

add_question(56,"Risk","Medium",
"A conservative investor may prefer:",
["Lower-risk investment options","Maximum volatility","No information","Highest fees"],
0,
"Risk preference affects investment choices.")

add_question(57,"Risk","Medium",
"Risk tolerance should be assessed:",
["Before making recommendations","After buying products","Only during claims","Never"],
0,
"Risk assessment helps determine suitability.")

add_question(58,"Guarantees","Easy",
"Guarantees are provided by:",
["The insurance contract","Market performance","Investment rumours","Other investors"],
0,
"Guarantees come from contract terms.")

add_question(59,"Guarantees","Medium",
"Guarantees may require:",
["Meeting contract conditions","Ignoring the contract","Frequent withdrawals","No premiums"],
0,
"Guarantees apply according to conditions.")

add_question(60,"Fees","Easy",
"Investment fees generally:",
["Reduce returns","Increase guarantees","Remove risk","Create benefits"],
0,
"Fees reduce the amount earned by investors.")

add_question(61,"Fees","Medium",
"Fee disclosure helps clients:",
["Understand product costs","Avoid contracts","Guarantee returns","Remove taxes"],
0,
"Clients need transparency about costs.")

add_question(62,"Professional Conduct","Easy",
"An advisor should provide:",
["Clear information","False guarantees","Hidden fees","Pressure decisions"],
0,
"Clear communication supports informed decisions.")

add_question(63,"Professional Conduct","Medium",
"Misrepresentation means:",
["Providing false or misleading information","Explaining benefits","Reviewing needs","Comparing products"],
0,
"False information is unacceptable.")

add_question(64,"Professional Conduct","Easy",
"Client interests should come:",
["Before advisor compensation","After commissions","After sales goals","Last"],
0,
"Advice should prioritize client needs.")

add_question(65,"Beneficiaries","Medium",
"A beneficiary can receive:",
["Death benefit proceeds","Investment advice","Premium discounts","Tax refunds"],
0,
"Beneficiaries receive contract benefits.")

add_question(66,"Beneficiaries","Easy",
"A beneficiary designation should be:",
["Reviewed periodically","Ignored forever","Made randomly","Removed always"],
0,
"Life changes may require updates.")

add_question(67,"Estate Planning","Medium",
"Segregated funds may help with:",
["Estate planning","Vehicle financing","Mortgage approval","Employment contracts"],
0,
"Beneficiary features can support estate planning.")

add_question(68,"Estate Planning","Easy",
"A beneficiary may help:",
["Direct payment of benefits","Increase market returns","Remove fees","Change investments"],
0,
"Beneficiary designations direct benefit payments.")

add_question(69,"Contract Features","Medium",
"Contract guarantees are based on:",
["Specified dates and conditions","Market rumours","Advisor predictions","Client wishes only"],
0,
"Guarantees depend on contract rules.")

add_question(70,"Contract Features","Easy",
"Reading the contract helps clients:",
["Understand rights and obligations","Avoid investments","Guarantee profits","Remove risks"],
0,
"Contract knowledge is important.")

add_question(71,"Investment Features","Medium",
"Rebalancing a portfolio means:",
["Adjusting investment allocation","Ending the contract","Changing beneficiaries","Removing guarantees"],
0,
"Rebalancing changes investment proportions.")

add_question(72,"Investment Features","Easy",
"Diversification involves:",
["Spreading investments","Buying one asset only","Avoiding all investments","Removing insurance"],
0,
"Diversification spreads risk.")

add_question(73,"Basics","Medium",
"Segregated funds are regulated as:",
["Insurance products","Bank accounts","Loans","Government grants"],
0,
"Segregated funds are insurance contracts.")

add_question(74,"Basics","Easy",
"The insurer provides:",
["Contractual protection","Stock predictions","Tax refunds","Employment benefits"],
0,
"The insurer provides benefits stated in the contract.")

add_question(75,"Basics","Medium",
"Understanding client goals helps:",
["Select suitable products","Guarantee returns","Remove market changes","Avoid contracts"],
0,
"Recommendations should match client objectives.")



add_question(76,"Investment Features","Easy",
"A fund switch allows a client to:",
["Move money between investment options","End the contract automatically","Remove guarantees","Avoid all fees"],
0,
"Fund switches allow movement between available options.")

add_question(77,"Investment Features","Medium",
"Before switching funds, clients should consider:",
["Investment objectives and consequences","Only advertisements","Only commissions","Nothing"],
0,
"Fund choices should match client goals.")

add_question(78,"Risk","Easy",
"Investment diversification helps:",
["Reduce concentration risk","Guarantee profits","Remove contracts","Stop markets"],
0,
"Diversification can reduce concentration of risk.")

add_question(79,"Risk","Medium",
"An aggressive investor may accept:",
["Greater investment fluctuations","No market changes","Guaranteed returns","No risk"],
0,
"Riskier investments may have greater fluctuations.")

add_question(80,"Risk","Easy",
"A client's risk profile includes:",
["Risk tolerance and objectives","Favourite investments only","Income tax only","Age only"],
0,
"Risk profile considers several client factors.")

add_question(81,"Guarantees","Medium",
"A guarantee does not mean:",
["Unlimited investment growth","Protection under conditions","Contract protection","Specified benefits"],
0,
"Guarantees do not promise unlimited growth.")

add_question(82,"Guarantees","Easy",
"Guarantees are valuable because they:",
["Provide protection features","Eliminate investing","Control markets","Increase fees"],
0,
"Guarantees provide additional protection.")

add_question(83,"Fees","Medium",
"High fees may:",
["Reduce net returns","Increase guarantees","Remove risk","Improve markets"],
0,
"Fees affect the amount investors receive.")

add_question(84,"Fees","Easy",
"Fee information should be:",
["Provided clearly to clients","Hidden","Ignored","Changed secretly"],
0,
"Clients should understand costs.")

add_question(85,"Professional Conduct","Medium",
"Know-your-client requirements help advisors:",
["Understand client circumstances","Increase commissions","Avoid documentation","Guarantee results"],
0,
"Knowing the client supports suitable advice.")

add_question(86,"Professional Conduct","Easy",
"Documentation should be:",
["Accurate and complete","Optional always","Destroyed immediately","Hidden"],
0,
"Proper documentation supports compliance.")

add_question(87,"Professional Conduct","Medium",
"An advisor should avoid:",
["Conflicts of interest","Clear explanations","Client reviews","Documentation"],
0,
"Conflicts must be managed appropriately.")

add_question(88,"Contract Features","Easy",
"A contract owner should know:",
["Contract benefits and conditions","Only the product name","Only fees","Only returns"],
0,
"Understanding the contract is important.")

add_question(89,"Contract Features","Medium",
"Changing contract information may require:",
["Following insurer procedures","Ignoring the contract","Market approval","Government approval only"],
0,
"Changes must follow contract rules.")

add_question(90,"Beneficiaries","Easy",
"Beneficiary designations are important because:",
["They identify who receives benefits","They guarantee returns","They change investments","They remove fees"],
0,
"Beneficiaries receive contract benefits.")

add_question(91,"Estate Planning","Medium",
"Segregated funds may provide:",
["Efficient benefit transfer features","Guaranteed wealth","No taxes ever","No paperwork"],
0,
"Certain features may support estate planning.")

add_question(92,"Tax Features","Medium",
"Tax consequences should be considered when:",
["Making investment decisions","Ignoring contracts","Changing markets","Selecting colours"],
0,
"Tax considerations may affect decisions.")

add_question(93,"Investment Features","Easy",
"Investment objectives describe:",
["What the client wants to achieve","The advisor's goals","Market predictions","Government plans"],
0,
"Objectives guide recommendations.")

add_question(94,"Investment Features","Medium",
"Time horizon refers to:",
["How long money is invested","Investment fee amount","Contract colour","Beneficiary age"],
0,
"Time horizon affects investment choices.")

add_question(95,"Risk","Medium",
"A longer investment horizon may:",
["Allow more time for market changes","Guarantee profits","Remove all risk","Avoid contracts"],
0,
"Time horizon is a factor in investment planning.")

add_question(96,"Basics","Easy",
"Segregated funds provide:",
["Investment choices with insurance protection","Only savings accounts","Only loans","Only tax services"],
0,
"Segregated funds combine features.")

add_question(97,"Basics","Medium",
"The insurance component provides:",
["Contract guarantees","Market control","Government payments","Stock predictions"],
0,
"Insurance features provide contractual guarantees.")

add_question(98,"Professional Conduct","Easy",
"An advisor should recommend products based on:",
["Client needs","Highest commission","Personal preference","Market rumours"],
0,
"Recommendations should be suitable.")

add_question(99,"Professional Conduct","Medium",
"Suitability review should include:",
["Client goals, risk, and circumstances","Only age","Only income","Only investments"],
0,
"Suitability requires a complete client review.")

add_question(100,"Basics","Medium",
"Segregated funds are best described as:",
["Insurance contracts with investment features","Bank deposits","Loans","Government programs"],
0,
"They combine insurance protection with investment options.")



add_question(101,"Contract Features","Easy",
"The contract anniversary date is used to:",
["Track contract milestones","Guarantee profits","Change markets","Remove fees"],
0,
"Contract dates help determine features and benefits.")

add_question(102,"Contract Features","Medium",
"Contract information should be reviewed:",
["Regularly with the client","Never","Only after claims","Only after losses"],
0,
"Regular reviews help keep information accurate.")

add_question(103,"Investment Features","Easy",
"Investment portfolios contain:",
["Selected underlying investments","Only insurance fees","Only taxes","Only guarantees"],
0,
"Portfolios contain underlying investments.")

add_question(104,"Investment Features","Medium",
"Investment performance should be evaluated:",
["Against client objectives","Only against advertisements","Only against fees","Without information"],
0,
"Performance should be considered in relation to goals.")

add_question(105,"Risk","Easy",
"Risk and return are often:",
["Related","Identical","Unrelated always","Guaranteed"],
0,
"Higher potential returns often involve different levels of risk.")

add_question(106,"Risk","Medium",
"Investment risk can be managed by:",
["Diversification and planning","Ignoring markets","Removing contracts","Avoiding information"],
0,
"Planning and diversification help manage risk.")

add_question(107,"Guarantees","Easy",
"Guarantees are not the same as:",
["Market gains","Contract benefits","Insurance features","Specified protection"],
0,
"Guarantees provide protection, not unlimited gains.")

add_question(108,"Guarantees","Medium",
"A guarantee amount may depend on:",
["Premiums and contract terms","Stock predictions","Advisor opinion","Government changes"],
0,
"Guarantee calculations follow contract rules.")

add_question(109,"Withdrawals","Easy",
"Withdrawals reduce:",
["The amount invested","The beneficiary name","The advisor license","The market"],
0,
"Withdrawals remove money from the contract.")

add_question(110,"Withdrawals","Medium",
"Clients should understand withdrawal:",
["Effects on guarantees and values","Only paperwork","Only commissions","Only taxes"],
0,
"Withdrawals may affect benefits.")

add_question(111,"Beneficiaries","Easy",
"The beneficiary receives payment after:",
["The insured person's death according to contract terms","Every withdrawal","Market increase","Premium payment"],
0,
"Death benefits are paid according to contract provisions.")

add_question(112,"Beneficiaries","Medium",
"Beneficiary designations should consider:",
["Client wishes and estate goals","Market forecasts","Advisor preferences","Advertising"],
0,
"Beneficiary planning reflects client goals.")

add_question(113,"Estate Planning","Easy",
"Estate planning helps:",
["Organize transfer of assets","Increase market returns","Remove contracts","Avoid all taxes"],
0,
"Estate planning organizes asset transfer.")

add_question(114,"Estate Planning","Medium",
"Segregated funds may provide:",
["Creditor protection features in some situations","Guaranteed profits","No fees","No rules"],
0,
"Certain contracts may have creditor protection features.")

add_question(115,"Tax Features","Easy",
"Tax treatment depends on:",
["Applicable legislation","Market colour","Advisor choice","Investment name"],
0,
"Tax rules determine treatment.")

add_question(116,"Tax Features","Medium",
"Clients with tax questions should:",
["Seek appropriate professional advice","Ignore taxes","Change beneficiaries only","Avoid contracts"],
0,
"Tax advice may require specialists.")

add_question(117,"Professional Conduct","Easy",
"An advisor should:",
["Act professionally","Hide information","Promise results","Ignore needs"],
0,
"Professional conduct requires responsible behaviour.")

add_question(118,"Professional Conduct","Medium",
"Client records should be:",
["Maintained properly","Destroyed immediately","Shared publicly","Ignored"],
0,
"Proper records support compliance.")

add_question(119,"Professional Conduct","Easy",
"Disclosure means:",
["Providing relevant information","Hiding costs","Avoiding questions","Making promises"],
0,
"Disclosure helps clients make informed choices.")

add_question(120,"Professional Conduct","Medium",
"An advisor should explain:",
["Limitations as well as benefits","Only advantages","Only fees","Only risks"],
0,
"Balanced explanations are required.")

add_question(121,"Basics","Easy",
"Segregated funds are designed to:",
["Combine investment and insurance features","Replace all products","Remove markets","Guarantee wealth"],
0,
"They combine investment options and insurance protection.")

add_question(122,"Basics","Medium",
"The insurer's role is to:",
["Provide contractual insurance benefits","Control investments daily","Set stock prices","Choose beneficiaries"],
0,
"The insurer provides contract benefits.")

add_question(123,"Investment Features","Easy",
"An investment objective may include:",
["Growth or income goals","Guaranteed wealth","No planning","No risk"],
0,
"Objectives guide investment selection.")

add_question(124,"Investment Features","Medium",
"Asset mix refers to:",
["Distribution among investment categories","Contract ownership","Beneficiary choice","Premium dates"],
0,
"Asset mix describes portfolio allocation.")

add_question(125,"Risk","Medium",
"A balanced investor may prefer:",
["A mix of growth and protection","Only highest risk","No investments","Only cash"],
0,
"Balanced approaches combine different objectives.")



add_question(126,"Investment Features","Easy",
"A portfolio manager may:",
["Manage underlying investments","Guarantee profits","Change laws","Approve claims"],
0,
"Portfolio managers manage investment selections.")

add_question(127,"Investment Features","Medium",
"Investment choices should match:",
["Client objectives and risk profile","Advisor commission","Market rumours","Advertising"],
0,
"Choices should be suitable for the client.")

add_question(128,"Risk","Easy",
"Volatility means:",
["Changes in investment value","Guaranteed growth","Contract ownership","Insurance fees"],
0,
"Volatility describes price fluctuations.")

add_question(129,"Risk","Medium",
"Market downturns may:",
["Reduce investment values","Increase guarantees automatically","Remove contracts","Stop fees"],
0,
"Markets can affect investment values.")

add_question(130,"Guarantees","Easy",
"Guarantees provide:",
["Specified protection","Unlimited returns","No contract rules","Market control"],
0,
"Guarantees provide defined protection.")

add_question(131,"Guarantees","Medium",
"Guarantees should be explained with:",
["Contract conditions","Predictions","Opinions","Advertisements"],
0,
"Contract details determine guarantees.")

add_question(132,"Fees","Easy",
"Fees are disclosed to:",
["Help clients understand costs","Hide expenses","Increase returns","Remove risk"],
0,
"Disclosure supports informed decisions.")

add_question(133,"Fees","Medium",
"Lower fees may:",
["Improve net returns","Guarantee profits","Remove market risk","Change beneficiaries"],
0,
"Fees affect net investment results.")

add_question(134,"Withdrawals","Easy",
"A withdrawal is:",
["Removing money from the contract","Adding a beneficiary","Changing markets","Buying insurance"],
0,
"Withdrawals remove contract value.")

add_question(135,"Withdrawals","Medium",
"Frequent withdrawals may affect:",
["Contract guarantees","Advisor license","Government rules","Market operation"],
0,
"Withdrawals can reduce guarantees.")

add_question(136,"Beneficiaries","Easy",
"A beneficiary receives:",
["Contract benefits","Investment control","Advisor income","Premium refunds"],
0,
"Beneficiaries receive benefits under the contract.")

add_question(137,"Beneficiaries","Medium",
"Beneficiary choices should reflect:",
["Client intentions","Market timing","Advisor preference","Advertising"],
0,
"Beneficiary designation should follow client wishes.")

add_question(138,"Estate Planning","Easy",
"Estate planning involves:",
["Planning asset transfer","Predicting markets","Removing insurance","Avoiding contracts"],
0,
"Estate planning organizes distribution of assets.")

add_question(139,"Estate Planning","Medium",
"Segregated funds may help because of:",
["Insurance contract features","Stock ownership","Bank guarantees","Government payments"],
0,
"Insurance features may support planning goals.")

add_question(140,"Tax Features","Easy",
"Tax rules may change:",
["Over time","Never","By advisor choice","By market value"],
0,
"Tax legislation can change.")

add_question(141,"Tax Features","Medium",
"Tax advice should come from:",
["Qualified professionals when needed","Friends","Advertisements","Market reports"],
0,
"Specialized advice may be required.")

add_question(142,"Professional Conduct","Easy",
"An advisor should avoid:",
["Misleading statements","Clear explanations","Documentation","Client reviews"],
0,
"Misleading statements are unacceptable.")

add_question(143,"Professional Conduct","Medium",
"Good documentation protects:",
["Clients and advisors","Only markets","Only insurers","Only investments"],
0,
"Records support accountability.")

add_question(144,"Contract Features","Easy",
"Premiums are:",
["Payments made for the contract","Market returns","Beneficiary payments","Tax refunds"],
0,
"Premiums fund the insurance contract.")

add_question(145,"Contract Features","Medium",
"Premium amount may affect:",
["Contract value and guarantees","Market rules","Advisor license","Tax laws"],
0,
"Premiums can influence contract benefits.")

add_question(146,"Basics","Easy",
"Segregated funds are:",
["Insurance contracts with investments","Bank loans","Savings accounts only","Government programs"],
0,
"They are insurance-based investment products.")

add_question(147,"Basics","Medium",
"The main advantage of segregated funds is:",
["Combination of investment and insurance features","No market changes","Unlimited returns","No costs"],
0,
"They combine multiple features.")

add_question(148,"Investment Features","Easy",
"Investment statements show:",
["Account and investment information","Government rules","Advisor salary","Insurance claims only"],
0,
"Statements provide investment details.")

add_question(149,"Investment Features","Medium",
"Reviewing statements helps clients:",
["Monitor investments","Guarantee results","Remove risk","Avoid contracts"],
0,
"Reviews help track progress.")

add_question(150,"Professional Conduct","Medium",
"Regular client reviews help:",
["Keep recommendations suitable","Increase fees","Remove guarantees","Avoid documentation"],
0,
"Reviews help maintain suitability.")



add_question(151,"Investment Features","Easy",
"Investment performance reports help clients:",
["Understand investment progress","Guarantee returns","Remove fees","Change laws"],
0,
"Reports help clients monitor investments.")

add_question(152,"Investment Features","Medium",
"A client review should consider:",
["Changing needs and objectives","Only market news","Only fees","Only age"],
0,
"Client circumstances can change.")

add_question(153,"Risk","Easy",
"Risk assessment helps determine:",
["Suitable investments","Guaranteed profits","Contract dates","Tax rates"],
0,
"Risk assessment supports suitable recommendations.")

add_question(154,"Risk","Medium",
"Investment losses are possible because:",
["Markets fluctuate","Contracts disappear","Fees stop","Guarantees fail always"],
0,
"Market changes can affect investment values.")

add_question(155,"Guarantees","Easy",
"Guarantees are:",
["Contract-based protections","Market promises","Advisor opinions","Predictions"],
0,
"Guarantees come from the insurance contract.")

add_question(156,"Guarantees","Medium",
"Clients should understand guarantee:",
["Conditions and limitations","Only benefits","Only returns","Only fees"],
0,
"Guarantees have specific conditions.")

add_question(157,"Contract Features","Easy",
"The contract contains:",
["Rights and obligations","Stock prices","Tax laws only","Market forecasts"],
0,
"The contract defines responsibilities.")

add_question(158,"Contract Features","Medium",
"Reading the contract helps avoid:",
["Misunderstanding benefits","Investment growth","Client reviews","Documentation"],
0,
"Understanding terms is important.")

add_question(159,"Fees","Easy",
"Expense information should be:",
["Available to clients","Hidden","Ignored","Changed secretly"],
0,
"Clients should receive cost information.")

add_question(160,"Fees","Medium",
"Understanding fees helps clients:",
["Compare products properly","Guarantee returns","Avoid investments","Remove taxes"],
0,
"Fee awareness supports decisions.")

add_question(161,"Professional Conduct","Easy",
"Fair dealing means:",
["Treating clients honestly","Promising results","Hiding information","Ignoring concerns"],
0,
"Fair treatment is a professional obligation.")

add_question(162,"Professional Conduct","Medium",
"An advisor should explain:",
["Product limitations","Only advantages","Only commissions","Only risks"],
0,
"Clients need balanced information.")

add_question(163,"Beneficiaries","Easy",
"Beneficiary changes should be:",
["Properly documented","Ignored","Secret from everyone","Automatic"],
0,
"Changes require proper procedures.")

add_question(164,"Beneficiaries","Medium",
"Beneficiary planning is part of:",
["Estate planning","Market timing","Tax avoidance only","Investment trading"],
0,
"Beneficiary choices support estate goals.")

add_question(165,"Estate Planning","Easy",
"Estate planning considers:",
["Future transfer of assets","Daily market prices","Advisor income","Fees only"],
0,
"It focuses on asset distribution.")

add_question(166,"Estate Planning","Medium",
"Segregated funds may be attractive for:",
["Certain estate planning goals","Only short-term borrowing","Only businesses","No investors"],
0,
"Some features support estate planning.")

add_question(167,"Tax Features","Easy",
"Tax rules apply according to:",
["Current legislation","Advisor preference","Market movement","Client wishes only"],
0,
"Tax treatment follows laws.")

add_question(168,"Tax Features","Medium",
"Tax information should be:",
["Accurate and current","Ignored","Estimated randomly","Hidden"],
0,
"Accurate information is important.")

add_question(169,"Basics","Easy",
"Segregated funds include:",
["An insurance component","Only stocks","Only bonds","Only cash"],
0,
"The insurance component distinguishes them.")

add_question(170,"Basics","Medium",
"The insurer's guarantee is:",
["Defined in the contract","A market prediction","An advisor promise","Unlimited"],
0,
"Guarantees are contractual.")

add_question(171,"Investment Features","Easy",
"Clients invest according to:",
["Selected investment options","Random choices","Government instructions","Advisor income"],
0,
"Clients choose available options based on needs.")

add_question(172,"Investment Features","Medium",
"Investment strategy should consider:",
["Goals and risk tolerance","Only returns","Only fees","Only markets"],
0,
"Strategy should match client circumstances.")

add_question(173,"Risk","Easy",
"Risk tolerance can change because of:",
["Life circumstances","Market colours","Product names","Fees only"],
0,
"Client situations may change.")

add_question(174,"Risk","Medium",
"Regular reviews help identify:",
["Changes in client needs","Guaranteed profits","New laws only","No risks"],
0,
"Reviews keep advice suitable.")

add_question(175,"Professional Conduct","Medium",
"An advisor must maintain:",
["Professional standards","Market control","Guaranteed results","Secret fees"],
0,
"Professional standards are required.")




























add_question(176,"Risk","Easy",
"Understanding risk helps clients:",
["Make suitable investment decisions","Guarantee profits","Avoid all markets","Remove contracts"],
0,
"Risk awareness supports better decisions.")

add_question(177,"Risk","Medium",
"A client's investment decision should consider:",
["Risk tolerance and objectives","Only market news","Only fees","Only guarantees"],
0,
"Investment decisions should match client circumstances.")

add_question(178,"Contract Features","Easy",
"The insurance contract contains:",
["Terms and conditions","Market predictions","Government policies","Advisor opinions"],
0,
"The contract defines rights and obligations.")

add_question(179,"Contract Features","Medium",
"Contract limitations should be:",
["Explained clearly","Ignored","Hidden","Removed"],
0,
"Clients should understand limitations.")

add_question(180,"Guarantees","Easy",
"Guarantees apply:",
["According to contract terms","In every situation","Without conditions","Only during growth"],
0,
"Guarantees depend on the contract.")

add_question(181,"Guarantees","Medium",
"A guarantee review should include:",
["Dates, amounts, and conditions","Only returns","Only fees","Only risks"],
0,
"Guarantee details should be reviewed.")

add_question(182,"Investment Features","Easy",
"Investment choices should be:",
["Appropriate for client goals","Based on rumours","Selected randomly","Always aggressive"],
0,
"Suitability is important.")

add_question(183,"Investment Features","Medium",
"Changing investment choices may affect:",
["Portfolio performance and risk","Contract ownership","Government rules","Beneficiary identity"],
0,
"Investment changes affect outcomes.")

add_question(184,"Fees","Easy",
"Clients should know:",
["All applicable fees","Only profits","Only guarantees","Nothing"],
0,
"Fee awareness is important.")

add_question(185,"Fees","Medium",
"Fees should be compared with:",
["Product benefits and services","Market rumours","Advisor income","Government programs"],
0,
"Clients should evaluate value received.")

add_question(186,"Professional Conduct","Easy",
"An advisor must:",
["Provide honest information","Guarantee returns","Hide risks","Ignore clients"],
0,
"Honesty is a professional obligation.")

add_question(187,"Professional Conduct","Medium",
"Good communication includes:",
["Explaining risks and benefits","Only selling","Avoiding questions","Making promises"],
0,
"Clients need complete explanations.")

add_question(188,"Professional Conduct","Easy",
"Client needs should be:",
["Reviewed regularly","Ignored","Assumed","Hidden"],
0,
"Regular reviews help maintain suitability.")

add_question(189,"Beneficiaries","Medium",
"Beneficiary designations can be:",
["Changed according to contract rules","Changed secretly","Ignored forever","Guaranteed returns"],
0,
"Changes follow contract requirements.")

add_question(190,"Estate Planning","Easy",
"Estate planning goals include:",
["Organizing asset transfer","Predicting markets","Removing investments","Avoiding advice"],
0,
"Estate planning organizes distribution.")

add_question(191,"Tax Features","Medium",
"Tax considerations may affect:",
["Investment decisions","Market prices","Insurance guarantees","Advisor licenses"],
0,
"Tax rules may influence planning.")

add_question(192,"Basics","Easy",
"Segregated funds are offered by:",
["Insurance companies","Stock exchanges","Government offices","Employers"],
0,
"Insurance companies offer segregated funds.")

add_question(193,"Basics","Medium",
"Segregated funds are different from regular investments because of:",
["Insurance guarantees","No investments","No contracts","No fees"],
0,
"They include insurance features.")

add_question(194,"Investment Features","Easy",
"Investment returns are affected by:",
["Market performance","Beneficiary choice","Contract paperwork","Advisor location"],
0,
"Markets affect investment returns.")

add_question(195,"Investment Features","Medium",
"Investors should review:",
["Performance and objectives","Only returns","Only fees","Only guarantees"],
0,
"Reviews compare results with goals.")

add_question(196,"Contract Features","Easy",
"Premium payments are required according to:",
["Contract terms","Market rumours","Advisor choice","Government wishes"],
0,
"Premium requirements are stated in the contract.")

add_question(197,"Contract Features","Medium",
"Failing to meet contract requirements may:",
["Affect benefits","Increase guarantees","Remove fees","Improve returns"],
0,
"Contract conditions must be followed.")

add_question(198,"Professional Conduct","Easy",
"An advisor should recommend:",
["Suitable products","Highest commission products","Random products","Only popular products"],
0,
"Recommendations must be suitable.")

add_question(199,"Professional Conduct","Medium",
"Client documentation should show:",
["Reasons for recommendations","Only sales numbers","Only fees","Market predictions"],
0,
"Documentation supports suitability.")

add_question(200,"Basics","Medium",
"The purpose of segregated funds is to:",
["Provide investment options with insurance protection","Guarantee all profits","Remove all risk","Replace every insurance product"],
0,
"Segregated funds combine investment opportunities with insurance protection.")


with open(output,"w") as f:
    json.dump(questions,f,indent=2)

print("Generated questions:",len(questions))
