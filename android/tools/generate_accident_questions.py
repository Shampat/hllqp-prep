import json

output = "app/src/main/assets/questions/accident_sickness_questions.json"

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
        "moduleId": "accident",
        "moduleName": "Accident & Sickness Insurance",
        "topic": topic,
        "difficulty": difficulty,
        "question": question,
        "options": options,
        "correctAnswer": correct,
        "explanation": explanation
    })




add_question(
    1,
    "Basics",
    "Easy",
    "What is the main purpose of accident and sickness insurance?",
    [
        "Provide financial protection against illness or injury",
        "Guarantee investment returns",
        "Replace all government benefits",
        "Eliminate all medical costs"
    ],
    0,
    "Accident and sickness insurance helps protect against financial loss caused by illness or injury."
)

add_question(
    2,
    "Disability Insurance",
    "Easy",
    "Disability insurance is designed primarily to:",
    [
        "Replace lost income during disability",
        "Provide retirement savings",
        "Increase investment returns",
        "Pay life insurance premiums"
    ],
    0,
    "Disability insurance provides income protection when a person cannot work due to disability."
)

add_question(
    3,
    "Disability Insurance",
    "Easy",
    "A disability benefit is paid when:",
    [
        "The insured meets the policy definition of disability",
        "The insured changes jobs",
        "The insured buys a home",
        "The insured retires"
    ],
    0,
    "Benefits are payable when the insured satisfies the disability requirements in the contract."
)

add_question(
    4,
    "Policy Features",
    "Medium",
    "The elimination period is:",
    [
        "The waiting period before benefits begin",
        "The policy renewal date",
        "The claim investigation period",
        "The premium payment date"
    ],
    0,
    "The elimination period is the waiting time before benefits start."
)

add_question(
    5,
    "Policy Features",
    "Medium",
    "A longer elimination period usually results in:",
    [
        "Lower premiums",
        "Higher guaranteed returns",
        "No coverage",
        "Automatic claim approval"
    ],
    0,
    "A longer waiting period generally lowers the cost of disability coverage."
)










add_question(6,"Disability Insurance","Medium",
"Own occupation disability coverage focuses on whether the insured can:",
["Perform their regular occupation","Work any available job","Retire early","Change insurers"],
0,
"Own occupation coverage considers the insured person's ability to perform their own occupation.")

add_question(7,"Disability Insurance","Medium",
"Any occupation disability coverage considers whether the insured can:",
["Perform another suitable occupation","Only perform their original job","Avoid medical assessments","Receive retirement benefits"],
0,
"Any occupation coverage considers whether the insured can work in suitable employment.")

add_question(8,"Premiums","Easy",
"Which factor may affect disability insurance premiums?",
["Age, health, and occupation","Favourite colour","Vehicle model only","Home decoration"],
0,
"Premiums are based on risk factors such as age, health, and occupation.")

add_question(9,"Benefits","Easy",
"A monthly disability benefit is intended to:",
["Replace part of lost income","Create investment gains","Pay only taxes","Replace retirement savings"],
0,
"Disability benefits help replace income when the insured cannot work.")

add_question(10,"Underwriting","Medium",
"The purpose of underwriting is to:",
["Evaluate insurance risk","Pay claims immediately","Guarantee employment","Remove policy conditions"],
0,
"Underwriting evaluates risk before coverage is issued.")

add_question(11,"Benefits","Easy",
"Short-term disability insurance generally provides:",
["Income protection for a limited period","Lifetime investment growth","Death benefits only","Property coverage"],
0,
"Short-term disability coverage provides benefits for shorter disability periods.")

add_question(12,"Benefits","Medium",
"Long-term disability insurance is designed for:",
["Extended periods of disability","Car repairs","Home purchases","Investment planning"],
0,
"Long-term disability insurance protects income during extended disabilities.")

add_question(13,"Policy Features","Medium",
"A benefit period refers to:",
["How long benefits may be paid","The application date","The premium amount","The underwriting decision"],
0,
"The benefit period determines how long payments can continue.")

add_question(14,"Policy Features","Easy",
"A policy exclusion is:",
["A condition not covered by the policy","A guaranteed benefit","A premium discount","A claim payment"],
0,
"Exclusions identify situations where coverage does not apply.")

add_question(15,"Claims","Medium",
"When making a disability claim, the insured usually must provide:",
["Proof of disability","Investment statements only","Tax returns only","Vehicle records"],
0,
"Claims require evidence supporting the disability.")

add_question(16,"Medical Coverage","Easy",
"Health insurance commonly helps cover:",
["Medical expenses","Investment losses","Mortgage payments","Business profits"],
0,
"Health insurance helps pay eligible medical costs.")

add_question(17,"Medical Coverage","Medium",
"A deductible is:",
["An amount paid before insurance pays benefits","A guaranteed refund","A policy cancellation fee","A commission"],
0,
"A deductible is the amount the insured pays before coverage begins.")

add_question(18,"Medical Coverage","Easy",
"Prescription drug coverage helps pay for:",
["Eligible medication costs","Investment products","Life insurance premiums","Real estate costs"],
0,
"Prescription coverage helps reduce medication expenses.")

add_question(19,"Travel Insurance","Easy",
"Travel insurance may provide protection for:",
["Emergency medical expenses while travelling","Stock market losses","Home renovations","Vehicle financing"],
0,
"Travel insurance can cover unexpected medical emergencies during travel.")

add_question(20,"Travel Insurance","Medium",
"A travel insurance claim normally requires:",
["Supporting documentation","A new insurance policy","Investment approval","Employment records"],
0,
"Claims require documents supporting the loss or expense.")

add_question(21,"Policy Features","Medium",
"A renewable policy allows:",
["Continuation of coverage under stated conditions","Automatic investment gains","No premiums forever","Removal of all exclusions"],
0,
"Renewable policies allow continuation according to contract terms.")

add_question(22,"Policy Features","Medium",
"A guaranteed renewable policy means:",
["The insurer cannot cancel coverage if premiums are paid","Benefits double every year","Claims are automatic","No underwriting exists"],
0,
"Guaranteed renewable policies protect the insured's right to continue coverage.")

add_question(23,"Underwriting","Medium",
"Medical information is collected during underwriting to:",
["Assess risk","Increase investments","Avoid contracts","Reduce benefits"],
0,
"Medical information helps determine eligibility and pricing.")

add_question(24,"Ethics","Medium",
"An advisor should recommend coverage based on:",
["Client needs and circumstances","Highest commission","Personal preference","Fastest sale"],
0,
"Recommendations should be suitable for the client.")

add_question(25,"Ethics","Medium",
"Client information should be:",
["Kept confidential","Shared publicly","Sold to others","Ignored"],
0,
"Insurance professionals must protect client confidentiality.")




add_question(26,"Ethics","Medium",
"An advisor should explain policy limitations to:",
["Help the client make an informed decision","Increase commissions","Avoid documentation","Speed up sales"],
0,
"Clients should understand both benefits and limitations of coverage.")

add_question(27,"Claims","Easy",
"A valid insurance claim should be:",
["Supported by accurate information","Based on guesses","Submitted without details","Changed after approval"],
0,
"Claims must contain truthful and complete information.")

add_question(28,"Disability Insurance","Medium",
"The definition of disability is important because it determines:",
["When benefits are payable","The agent commission","The policy colour","The investment return"],
0,
"The contract definition determines eligibility for benefits.")

add_question(29,"Disability Insurance","Easy",
"Residual disability benefits are designed for someone who:",
["Can work but has reduced income due to disability","Has no insurance","Changes careers voluntarily","Retires"],
0,
"Residual benefits may cover partial income loss.")

add_question(30,"Disability Insurance","Medium",
"Partial disability refers to:",
["A disability that limits but does not completely prevent work","A cancelled policy","A premium refund","A policy transfer"],
0,
"Partial disability allows benefits when the insured can still work in a limited capacity.")

add_question(31,"Policy Features","Easy",
"The policyowner is responsible for:",
["Paying premiums and maintaining the policy","Approving medical claims","Setting government rules","Managing hospitals"],
0,
"The policyowner controls ownership responsibilities.")

add_question(32,"Policy Features","Medium",
"A rider is:",
["An additional contract provision added to a policy","A claim payment","A premium tax","A medical exam"],
0,
"Riders modify or add benefits to an insurance policy.")

add_question(33,"Policy Features","Easy",
"A waiver of premium benefit may:",
["Waive premiums during qualifying disability","Increase investment returns","Cancel coverage","Remove beneficiaries"],
0,
"Some policies waive premiums when the insured becomes disabled.")

add_question(34,"Health Insurance","Easy",
"Health insurance primarily protects against:",
["Healthcare expenses","Investment losses","Property damage","Business debts"],
0,
"Health insurance helps cover eligible healthcare costs.")

add_question(35,"Health Insurance","Medium",
"A coordination of benefits provision helps:",
["Determine payment when multiple plans exist","Increase premiums","Cancel policies","Avoid claims"],
0,
"Coordination prevents duplicate payment between plans.")

add_question(36,"Health Insurance","Easy",
"An insured person should review coverage because:",
["Needs and circumstances may change","Policies never change","Claims are automatic","Premiums disappear"],
0,
"Regular reviews help ensure suitable protection.")

add_question(37,"Travel Insurance","Medium",
"Travel medical insurance is important because:",
["Government coverage may be limited outside the country","Travel is always free","Claims are guaranteed","It replaces life insurance"],
0,
"Travel medical insurance helps protect against foreign medical costs.")

add_question(38,"Travel Insurance","Easy",
"A travel insurance exclusion means:",
["Certain situations are not covered","All claims are approved","Premiums are refunded","Coverage doubles"],
0,
"Exclusions identify situations where benefits are unavailable.")

add_question(39,"Underwriting","Medium",
"Occupation affects disability insurance because:",
["Some occupations have different levels of risk","All jobs have identical risks","Occupation is never considered","It affects only taxes"],
0,
"Occupation risk can affect eligibility and premiums.")

add_question(40,"Underwriting","Medium",
"Hazardous activities may affect:",
["Eligibility and premiums","The spelling of the policy","The agent's license","Government benefits"],
0,
"High-risk activities can change insurance risk assessment.")

add_question(41,"Premiums","Easy",
"A premium is:",
["The amount paid for insurance coverage","The claim amount","The benefit period","The deductible"],
0,
"Premiums are payments required to maintain coverage.")

add_question(42,"Premiums","Medium",
"Premiums may increase because of:",
["Higher risk factors","Lower claims history","Better health","Younger age"],
0,
"Greater risk generally results in higher premiums.")

add_question(43,"Claims","Medium",
"Fraudulent claims are:",
["False claims made intentionally","Normal claims","Policy renewals","Premium payments"],
0,
"Insurance fraud involves intentionally providing false information.")

add_question(44,"Claims","Easy",
"An insurer reviews claims to:",
["Determine whether benefits are payable","Increase sales","Change occupations","Avoid contracts"],
0,
"Claims review confirms whether policy requirements are met.")

add_question(45,"Professional Conduct","Medium",
"An advisor must act in:",
["The client's best interest","Only the insurer's interest","Personal financial interest","No one's interest"],
0,
"Professional conduct requires acting ethically and fairly.")

add_question(46,"Professional Conduct","Medium",
"Suitability means:",
["Recommending appropriate coverage for the client","Selling the most expensive plan","Avoiding questions","Using the same plan for everyone"],
0,
"Recommendations should match client needs.")

add_question(47,"Professional Conduct","Easy",
"Client needs analysis helps determine:",
["Appropriate insurance coverage","Commission amounts only","Tax rates","Stock prices"],
0,
"Needs analysis supports suitable recommendations.")

add_question(48,"Policy Features","Medium",
"Policy wording should be:",
["Reviewed carefully by the client","Ignored completely","Changed by the advisor","Removed after purchase"],
0,
"Understanding policy wording helps clients know their coverage.")

add_question(49,"Policy Features","Easy",
"A beneficiary designation is commonly associated with:",
["Life insurance benefits","Disability income payments only","Travel expenses","Premium discounts"],
0,
"Beneficiaries are mainly associated with death benefits.")

add_question(50,"Basics","Easy",
"Insurance transfers financial risk from:",
["The insured to the insurer","The insurer to the client","The government to the advisor","The client to another client"],
0,
"Insurance transfers certain risks in exchange for premiums.")




add_question(51,"Disability Insurance","Medium",
"Disability insurance is designed to protect:",
["Income earning ability","Investment portfolios","Vehicle value","Real estate prices"],
0,
"Disability insurance protects income when a person cannot work.")

add_question(52,"Disability Insurance","Easy",
"The insured under a disability policy is:",
["The person covered by the policy","The insurance company","The advisor","The beneficiary only"],
0,
"The insured is the person whose disability triggers benefits.")

add_question(53,"Disability Insurance","Medium",
"A disability policy benefit amount is usually based on:",
["A percentage of income","The agent's choice","The value of a vehicle","The client's investments"],
0,
"Benefits are commonly designed to replace part of earned income.")

add_question(54,"Disability Insurance","Medium",
"Occupation class affects disability insurance because:",
["Different jobs have different risks","All occupations have equal risk","It affects only taxes","It determines beneficiaries"],
0,
"Risk levels vary between occupations.")

add_question(55,"Disability Insurance","Easy",
"A waiting period before disability benefits begin is called:",
["Elimination period","Benefit period","Renewal period","Grace period"],
0,
"The elimination period is the waiting time before payments start.")

add_question(56,"Policy Features","Medium",
"The benefit period determines:",
["How long benefits may continue","The premium due date","The medical exam date","The application method"],
0,
"The benefit period specifies the duration of payable benefits.")

add_question(57,"Policy Features","Easy",
"A policy application should contain:",
["Accurate information","False information","Incomplete details","Unknown facts"],
0,
"Applications must be complete and truthful.")

add_question(58,"Underwriting","Medium",
"Underwriting helps insurers:",
["Assess risk before issuing coverage","Avoid all claims","Increase taxes","Remove contracts"],
0,
"Underwriting determines acceptable risk.")

add_question(59,"Underwriting","Easy",
"A medical examination may be required to:",
["Assess health risk","Determine employment","Set investment returns","Choose beneficiaries"],
0,
"Medical information helps evaluate insurance risk.")

add_question(60,"Underwriting","Medium",
"Misrepresentation on an application may:",
["Affect coverage or claims","Increase benefits automatically","Reduce premiums forever","Guarantee approval"],
0,
"Incorrect information can affect policy validity.")

add_question(61,"Health Insurance","Easy",
"Extended health benefits may cover:",
["Prescription drugs and medical services","Stock purchases","Home repairs","Vehicle loans"],
0,
"Extended health plans cover eligible healthcare expenses.")

add_question(62,"Health Insurance","Medium",
"A health insurance deductible means:",
["The insured pays an amount before benefits apply","The insurer pays everything immediately","The policy is cancelled","Premiums are refunded"],
0,
"A deductible is the initial amount paid by the insured.")

add_question(63,"Health Insurance","Easy",
"A co-payment means:",
["The insured shares part of the cost","The insurer receives money","The policy ends","The claim is rejected"],
0,
"Co-payments require the insured to pay part of an expense.")

add_question(64,"Health Insurance","Medium",
"Maximum benefit limits describe:",
["The highest amount payable under coverage","The premium amount","The application date","The advisor fee"],
0,
"Policies often limit the maximum payable benefit.")

add_question(65,"Health Insurance","Easy",
"Health insurance claims should include:",
["Proof of eligible expenses","Investment statements","Property records","Employment contracts"],
0,
"Documentation supports healthcare claims.")

add_question(66,"Travel Insurance","Medium",
"Travel insurance should generally be purchased:",
["Before travelling","After a claim occurs","After returning home","Only after illness"],
0,
"Travel insurance must usually be arranged before travel begins.")

add_question(67,"Travel Insurance","Easy",
"Emergency medical travel coverage helps with:",
["Unexpected medical expenses abroad","Investment losses","Vehicle damage only","Retirement income"],
0,
"Emergency medical coverage protects travellers from unexpected healthcare costs.")

add_question(68,"Travel Insurance","Medium",
"A travel insurance exclusion may apply to:",
["Certain pre-existing conditions","All emergencies","All travellers","Every medical expense"],
0,
"Policies may exclude certain conditions or situations.")

add_question(69,"Professional Conduct","Medium",
"An advisor should explain:",
["Benefits, costs, and limitations","Only advantages","Only commissions","Only exclusions"],
0,
"Clients need balanced information to make decisions.")

add_question(70,"Professional Conduct","Easy",
"Client consent is important when:",
["Collecting personal information","Changing laws","Setting taxes","Creating investments"],
0,
"Consent is required for proper handling of client information.")

add_question(71,"Professional Conduct","Medium",
"Privacy rules require advisors to:",
["Protect client information","Share information freely","Ignore records","Publish applications"],
0,
"Client privacy must be maintained.")

add_question(72,"Claims","Medium",
"Claim forms should be completed:",
["Accurately and honestly","With missing information","By guessing","Without signatures"],
0,
"Accurate claim information supports proper assessment.")

add_question(73,"Claims","Easy",
"The insurer may investigate a claim to:",
["Confirm eligibility for benefits","Increase premiums only","Avoid all payments","Change the contract"],
0,
"Claims investigation confirms policy requirements.")

add_question(74,"Basics","Easy",
"Insurance provides protection by:",
["Managing financial risk","Guaranteeing wealth","Removing all expenses","Creating investments"],
0,
"Insurance helps manage financial uncertainty.")

add_question(75,"Basics","Medium",
"Risk pooling allows insurers to:",
["Spread losses among many policyholders","Eliminate all claims","Avoid premiums","Guarantee profits"],
0,
"Insurance works by pooling risks among many insured people.")




add_question(76,"Basics","Easy",
"The purpose of insurance is to:",
["Provide financial protection against specified risks","Guarantee profits","Eliminate every expense","Replace all savings"],
0,
"Insurance helps protect against financial consequences of risks.")

add_question(77,"Basics","Medium",
"An insurance contract is based on:",
["Agreement between insurer and insured","A verbal promise only","Investment performance","Government ownership"],
0,
"Insurance is a contractual agreement between parties.")

add_question(78,"Policy Features","Medium",
"The policy schedule contains:",
["Important policy details","Medical advice","Investment forecasts","Government regulations"],
0,
"The policy schedule summarizes key contract information.")

add_question(79,"Policy Features","Easy",
"A premium payment keeps coverage:",
["In force","Cancelled","Transferred automatically","Guaranteed forever"],
0,
"Premiums maintain active insurance coverage.")

add_question(80,"Policy Features","Medium",
"A lapse occurs when:",
["Coverage ends because required premiums are not paid","Benefits increase","A claim is approved","A policy is upgraded"],
0,
"A policy may lapse when premiums are not maintained.")

add_question(81,"Disability Insurance","Medium",
"Disability income benefits are intended to:",
["Support living expenses during disability","Create retirement wealth","Pay investment losses","Replace all government programs"],
0,
"Benefits help maintain income during disability.")

add_question(82,"Disability Insurance","Easy",
"A waiting period exists mainly to:",
["Determine when benefits begin","Increase claim amounts","Remove exclusions","Avoid underwriting"],
0,
"The waiting period delays the start of benefit payments.")

add_question(83,"Disability Insurance","Medium",
"Occupation risk is considered because:",
["Some occupations have greater chance of injury","All jobs are identical","It affects beneficiaries","It determines taxes"],
0,
"Occupation is an important disability risk factor.")

add_question(84,"Disability Insurance","Easy",
"Disability benefits are generally paid:",
["According to policy terms","Automatically forever","Without proof","Only at retirement"],
0,
"Benefits depend on meeting contract conditions.")

add_question(85,"Disability Insurance","Medium",
"A recurring disability provision may help when:",
["A disability returns after recovery","A policy is cancelled","Premiums increase","A claim is denied"],
0,
"Recurring disability provisions address returning disabilities.")

add_question(86,"Health Insurance","Easy",
"Health insurance helps manage:",
["Healthcare costs","Investment risks","Property taxes","Business profits"],
0,
"Health insurance provides financial assistance for healthcare expenses.")

add_question(87,"Health Insurance","Medium",
"Pre-authorization may be required before:",
["Certain medical treatments","Buying groceries","Changing jobs","Paying premiums"],
0,
"Some treatments require approval before coverage applies.")

add_question(88,"Health Insurance","Easy",
"A health benefit claim should be:",
["Supported by receipts or documents","Based on estimates only","Submitted without details","Made verbally only"],
0,
"Documentation supports health claims.")

add_question(89,"Health Insurance","Medium",
"A benefit maximum means:",
["The limit payable under the policy","Unlimited coverage","A premium discount","A policy cancellation"],
0,
"Benefit maximums limit the amount payable.")

add_question(90,"Health Insurance","Easy",
"Preventive healthcare focuses on:",
["Maintaining and improving health","Increasing premiums","Replacing income","Avoiding insurance"],
0,
"Preventive care helps maintain health and detect issues early.")

add_question(91,"Travel Insurance","Medium",
"Travel insurance is designed for:",
["Unexpected travel-related risks","Investment planning","Home ownership","Employment changes"],
0,
"Travel insurance protects against certain travel risks.")

add_question(92,"Travel Insurance","Easy",
"Travel cancellation coverage may reimburse:",
["Eligible prepaid travel costs","All purchases","Investment losses","Mortgage payments"],
0,
"Cancellation coverage may protect eligible prepaid expenses.")

add_question(93,"Travel Insurance","Medium",
"Travellers should review exclusions because:",
["Some situations may not be covered","All claims are guaranteed","Premiums disappear","Coverage doubles"],
0,
"Understanding exclusions prevents misunderstandings.")

add_question(94,"Professional Conduct","Medium",
"An advisor should document:",
["Important client recommendations","Personal opinions only","Private conversations unrelated to advice","Nothing"],
0,
"Documentation supports professional practice.")

add_question(95,"Professional Conduct","Easy",
"Ethical selling requires:",
["Honest and suitable recommendations","Pressure tactics","Hidden information","False promises"],
0,
"Ethical sales practices protect clients.")

add_question(96,"Claims","Medium",
"Claim decisions are based on:",
["Policy terms and evidence","Agent preference","Client popularity","Market conditions"],
0,
"Claims are assessed according to the contract.")

add_question(97,"Claims","Easy",
"An insurer paying a valid claim demonstrates:",
["Contractual obligation","Investment activity","Tax planning","Employment service"],
0,
"Insurers pay valid claims according to policy agreements.")

add_question(98,"Underwriting","Medium",
"Risk classification helps insurers:",
["Set appropriate coverage terms","Remove all policies","Avoid customers","Guarantee claims"],
0,
"Risk classification helps determine suitable terms.")

add_question(99,"Underwriting","Easy",
"Accurate medical information helps:",
["Proper underwriting","Higher commissions","Automatic approval","Lower taxes"],
0,
"Accurate information allows proper risk assessment.")

add_question(100,"Basics","Medium",
"The insured should understand:",
["Coverage, exclusions, and obligations","Only the premium","Only the company name","Only the claim form"],
0,
"Understanding the contract helps clients make informed decisions.")




add_question(101,"Disability Insurance","Medium",
"The purpose of disability income insurance is to protect:",
["Earned income","Investment returns","Property value","Business ownership"],
0,
"Disability insurance protects income when illness or injury prevents working.")

add_question(102,"Disability Insurance","Easy",
"A total disability generally means:",
["The insured cannot perform work as defined by the policy","The insured changes jobs","The insured retires","The insured moves homes"],
0,
"Total disability depends on the policy definition.")

add_question(103,"Disability Insurance","Medium",
"A partial disability benefit may apply when:",
["The insured can work but earns less due to disability","The insured is unemployed by choice","The policy expires","The insured changes insurers"],
0,
"Partial disability benefits address reduced income caused by disability.")

add_question(104,"Disability Insurance","Medium",
"A residual benefit is commonly based on:",
["Loss of income","Age only","Investment value","Property damage"],
0,
"Residual benefits often consider income loss.")

add_question(105,"Disability Insurance","Easy",
"Disability insurance helps protect against:",
["Loss of earning ability","Stock market changes","Home repairs","Vehicle depreciation"],
0,
"The main purpose is income protection.")

add_question(106,"Policy Features","Medium",
"A policy rider can:",
["Add or modify coverage","Remove all premiums","Guarantee investments","Replace the contract"],
0,
"Riders change or add policy provisions.")

add_question(107,"Policy Features","Easy",
"The policy owner has the right to:",
["Control policy decisions","Approve medical claims","Set insurance laws","Change government rules"],
0,
"The policy owner controls contractual rights.")

add_question(108,"Policy Features","Medium",
"A grace period allows:",
["Additional time to pay premiums","Automatic benefit increases","Removal of exclusions","Free coverage"],
0,
"Grace periods allow continued coverage while overdue premiums are paid.")

add_question(109,"Policy Features","Easy",
"A beneficiary is a person who:",
["Receives benefits when designated by the policy","Pays premiums","Underwrites policies","Creates contracts"],
0,
"Beneficiaries receive designated policy proceeds.")

add_question(110,"Policy Features","Medium",
"Policy exclusions are included to:",
["Identify situations not covered","Increase claims","Remove premiums","Guarantee payment"],
0,
"Exclusions define limits of coverage.")

add_question(111,"Health Insurance","Easy",
"Health insurance may cover:",
["Hospital and medical expenses","Investment losses","Mortgage payments","Business profits"],
0,
"Health plans help cover eligible medical expenses.")

add_question(112,"Health Insurance","Medium",
"An insured should keep health receipts because:",
["They support claims","They increase benefits","They replace policies","They reduce premiums automatically"],
0,
"Receipts provide evidence of eligible expenses.")

add_question(113,"Health Insurance","Easy",
"A medical expense claim requires:",
["Eligible expenses and documentation","Investment records","Property records","Employment contracts"],
0,
"Claims require proof of covered expenses.")

add_question(114,"Health Insurance","Medium",
"A health insurance provider determines payment based on:",
["Policy coverage","Personal preference","Market prices","Employment status"],
0,
"Payments depend on the insurance contract.")

add_question(115,"Health Insurance","Easy",
"Coverage limits describe:",
["Maximum benefits available","Unlimited payments","Premium refunds","Policy ownership"],
0,
"Coverage limits define how much may be paid.")

add_question(116,"Travel Insurance","Medium",
"Travel medical insurance protects against:",
["Unexpected medical costs while travelling","Stock losses","Home repairs","Employment changes"],
0,
"Travel medical coverage protects travellers from medical emergencies.")

add_question(117,"Travel Insurance","Easy",
"Before purchasing travel insurance, clients should review:",
["Coverage and exclusions","Only the price","Only the company logo","Only advertisements"],
0,
"Reviewing coverage helps clients understand protection.")

add_question(118,"Travel Insurance","Medium",
"A pre-existing condition may:",
["Affect coverage eligibility","Increase benefits automatically","Remove premiums","Guarantee payment"],
0,
"Pre-existing conditions may have special policy rules.")

add_question(119,"Claims","Medium",
"A claim should be submitted:",
["Within required policy timelines","After coverage ends","Without documents","Only verbally"],
0,
"Policies often require claims to be submitted within specific periods.")

add_question(120,"Claims","Easy",
"Claim information should be:",
["Truthful and complete","Changed to improve approval","Hidden","Estimated"],
0,
"Accurate claim information is required.")

add_question(121,"Claims","Medium",
"Claim investigation helps:",
["Verify policy requirements","Increase premiums","Cancel all claims","Change beneficiaries"],
0,
"Insurers investigate claims to confirm eligibility.")

add_question(122,"Claims","Easy",
"A denied claim means:",
["The insurer determined policy requirements were not met","The policy is always cancelled","Premiums are refunded","Coverage never existed"],
0,
"A claim may be denied when contract requirements are not satisfied.")

add_question(123,"Professional Conduct","Medium",
"An advisor should avoid:",
["Misleading statements","Explaining benefits","Reviewing needs","Documenting advice"],
0,
"Advisors must communicate honestly.")

add_question(124,"Professional Conduct","Easy",
"Client needs should be reviewed:",
["Before recommending coverage","After selling only","Never","Only after claims"],
0,
"Needs analysis supports suitable recommendations.")

add_question(125,"Professional Conduct","Medium",
"Professional advisors maintain:",
["Competence and ethical standards","Secret pricing methods","Personal guarantees","Unverified information"],
0,
"Professional standards require knowledge and ethical behaviour.")




add_question(126,"Basics","Medium",
"Insurance is based on the principle of:",
["Sharing and transferring risk","Guaranteeing profits","Avoiding all uncertainty","Eliminating expenses"],
0,
"Insurance allows risks to be transferred and shared.")

add_question(127,"Basics","Easy",
"The insurer is the company that:",
["Provides insurance coverage","Receives disability benefits","Owns every policy","Sets personal goals"],
0,
"The insurer provides the contractual coverage.")

add_question(128,"Basics","Easy",
"The insured is the person who:",
["Receives protection under the policy","Always owns the company","Approves all claims","Sets premiums"],
0,
"The insured receives coverage under the contract.")

add_question(129,"Policy Features","Medium",
"A policy renewal allows:",
["Continuation of coverage according to terms","Automatic benefit doubling","Removal of all exclusions","No premium payments"],
0,
"Renewal continues coverage under policy conditions.")

add_question(130,"Policy Features","Easy",
"A policy contract should be:",
["Read and understood by the client","Ignored after purchase","Changed without approval","Shared publicly"],
0,
"Clients should understand their insurance contract.")

add_question(131,"Disability Insurance","Medium",
"Disability benefits are intended to help with:",
["Income replacement","Investment growth","Property repairs","Vehicle expenses"],
0,
"Benefits help replace income during disability.")

add_question(132,"Disability Insurance","Medium",
"The amount of disability coverage should consider:",
["Income and financial needs","Favourite hobbies only","Vehicle type","Home colour"],
0,
"Coverage should match the client's financial situation.")

add_question(133,"Disability Insurance","Easy",
"Disability insurance is most important for people who depend on:",
["Employment income","Lottery winnings","Property sales","Investment speculation"],
0,
"Employment income protection is the key purpose.")

add_question(134,"Health Insurance","Medium",
"Health insurance helps reduce:",
["Out-of-pocket medical expenses","Investment risk","Property taxes","Business expenses"],
0,
"Health coverage helps manage healthcare costs.")

add_question(135,"Health Insurance","Easy",
"A medical expense must usually be:",
["Eligible under the policy","Approved by an employer only","A personal investment","A tax payment"],
0,
"Only eligible expenses are covered.")

add_question(136,"Health Insurance","Medium",
"A policy maximum limits:",
["The amount payable","The client's age","The policy owner's rights","The advisor's license"],
0,
"Maximums define benefit limits.")

add_question(137,"Travel Insurance","Easy",
"Travel insurance protects against:",
["Unexpected travel risks","Guaranteed vacations","Investment changes","Career changes"],
0,
"Travel coverage protects against certain unexpected events.")

add_question(138,"Travel Insurance","Medium",
"Emergency assistance services may help with:",
["Finding medical support while travelling","Investment advice","Buying property","Changing jobs"],
0,
"Travel assistance helps during emergencies.")

add_question(139,"Underwriting","Medium",
"An insurer uses underwriting to determine:",
["Risk and policy terms","Vacation plans","Employment contracts","Investment returns"],
0,
"Underwriting evaluates risk before coverage.")

add_question(140,"Underwriting","Easy",
"Risk information should be:",
["Accurate and complete","Hidden from the insurer","Changed later","Based on guesses"],
0,
"Accurate information supports proper underwriting.")

add_question(141,"Claims","Medium",
"The purpose of claim forms is to:",
["Collect information about a loss","Increase premiums","Create investments","Cancel policies"],
0,
"Claim forms collect required details.")

add_question(142,"Claims","Easy",
"A valid claim should match:",
["The policy requirements","Personal preference","Market conditions","Agent opinion"],
0,
"Claims must meet contract requirements.")

add_question(143,"Professional Conduct","Medium",
"An advisor should provide:",
["Clear and accurate information","False guarantees","Hidden details","Pressure tactics"],
0,
"Clients require honest communication.")

add_question(144,"Professional Conduct","Easy",
"Confidential client information should be:",
["Protected","Published","Sold","Ignored"],
0,
"Privacy protection is a professional responsibility.")

add_question(145,"Professional Conduct","Medium",
"Conflict of interest should be:",
["Disclosed and managed","Ignored","Hidden","Encouraged"],
0,
"Conflicts should be handled transparently.")

add_question(146,"Premiums","Easy",
"Premiums are paid in exchange for:",
["Insurance protection","Investment ownership","Government benefits","Employment"],
0,
"Premiums purchase insurance coverage.")

add_question(147,"Premiums","Medium",
"A higher-risk applicant may have:",
["Higher premiums","Automatic approval","Lower benefits only","No underwriting"],
0,
"Risk level can affect premium cost.")

add_question(148,"Policy Features","Easy",
"An insurance policy contains:",
["Rights and obligations","Only advertisements","Investment promises","Government rules"],
0,
"The contract defines responsibilities of both parties.")

add_question(149,"Policy Features","Medium",
"Understanding exclusions helps clients know:",
["What is not covered","How to invest","How to avoid premiums","How to change laws"],
0,
"Exclusions explain coverage limitations.")

add_question(150,"Basics","Medium",
"Insurance decisions should be based on:",
["Individual needs and circumstances","Sales pressure","Random choices","Market rumours"],
0,
"Insurance should match the client's situation.")




add_question(151,"Disability Insurance","Medium",
"Disability insurance helps protect a person's:",
["Ability to earn income","Investment portfolio","Vehicle value","Home decoration"],
0,
"Disability coverage protects earning ability.")

add_question(152,"Disability Insurance","Easy",
"A disability claim usually requires:",
["Proof of disability","Investment statements","Property records","Travel documents"],
0,
"Evidence is needed to support disability claims.")

add_question(153,"Disability Insurance","Medium",
"Benefit payments may stop when:",
["The benefit period ends or policy conditions are met","The insured changes address","Premiums increase elsewhere","The advisor retires"],
0,
"Benefits continue only according to policy terms.")

add_question(154,"Disability Insurance","Medium",
"Disability insurance planning should consider:",
["Current income and expenses","Favourite activities only","Vehicle ownership","Home design"],
0,
"Financial needs determine suitable coverage.")

add_question(155,"Disability Insurance","Easy",
"A disability policy is designed mainly for:",
["Income protection","Investment growth","Property replacement","Tax reduction"],
0,
"The primary purpose is protecting income.")

add_question(156,"Health Insurance","Medium",
"Health coverage may include:",
["Dental or vision benefits when provided","Stock investments","Mortgage protection","Business ownership"],
0,
"Some health plans include additional medical services.")

add_question(157,"Health Insurance","Easy",
"Healthcare receipts are important because they:",
["Support reimbursement claims","Increase coverage automatically","Remove deductibles","Replace policies"],
0,
"Receipts provide proof of expenses.")

add_question(158,"Health Insurance","Medium",
"Coordination of benefits prevents:",
["Duplicate payment of expenses","All insurance coverage","Policy renewal","Medical treatment"],
0,
"It coordinates payments when multiple plans exist.")

add_question(159,"Health Insurance","Easy",
"An insured should know:",
["What services are covered","Only the premium amount","Only the insurer name","Only the claim number"],
0,
"Understanding coverage helps avoid surprises.")

add_question(160,"Health Insurance","Medium",
"Health insurance exclusions identify:",
["Services or conditions not covered","Additional premiums","Investment choices","Employment rules"],
0,
"Exclusions define limitations.")

add_question(161,"Travel Insurance","Easy",
"Travel insurance should be reviewed before:",
["Leaving for a trip","Filing a claim","Returning home","Changing jobs"],
0,
"Coverage should be arranged before travel.")

add_question(162,"Travel Insurance","Medium",
"Travel medical coverage may include:",
["Emergency hospital treatment","Investment advice","Home renovations","Business loans"],
0,
"Travel medical policies cover eligible emergencies.")

add_question(163,"Travel Insurance","Easy",
"Travel insurance does not normally guarantee:",
["Every possible expense will be paid","Emergency protection","Policy coverage","Claim review"],
0,
"Coverage depends on policy terms and exclusions.")

add_question(164,"Claims","Medium",
"Supporting documents help insurers:",
["Review claim validity","Increase premiums","Change laws","Create contracts"],
0,
"Documents help verify claims.")

add_question(165,"Claims","Easy",
"A claim should be reported:",
["According to policy requirements","Only after policy ends","Without information","To another company"],
0,
"Policies often specify reporting procedures.")

add_question(166,"Claims","Medium",
"Insurance fraud can result in:",
["Claim denial or legal consequences","Automatic benefits","Lower premiums","Extra coverage"],
0,
"Fraud has serious consequences.")

add_question(167,"Professional Conduct","Easy",
"Advisors should provide:",
["Professional advice","False promises","Hidden information","Personal guarantees"],
0,
"Professional advice must be honest and suitable.")

add_question(168,"Professional Conduct","Medium",
"A client's personal information should be collected:",
["For legitimate insurance purposes","For public sharing","For marketing without permission","For unrelated uses"],
0,
"Information should only be collected appropriately.")

add_question(169,"Professional Conduct","Medium",
"Good communication helps clients:",
["Understand insurance decisions","Avoid all documentation","Guarantee claims","Remove exclusions"],
0,
"Clear communication improves understanding.")

add_question(170,"Professional Conduct","Easy",
"A suitable recommendation considers:",
["Client needs","Maximum commission","Advisor preference","Random selection"],
0,
"Recommendations should be client-focused.")

add_question(171,"Basics","Medium",
"Insurance risk refers to:",
["Possibility of financial loss","Guaranteed profit","Investment growth","Employment status"],
0,
"Insurance addresses potential financial losses.")

add_question(172,"Basics","Easy",
"The purpose of premiums is to:",
["Pay for insurance protection","Create government funds","Guarantee returns","Remove all risks"],
0,
"Premiums fund insurance coverage.")

add_question(173,"Basics","Medium",
"Insurance contracts require:",
["Both parties to follow agreed terms","No documentation","No responsibilities","No premiums"],
0,
"Contracts create obligations for both parties.")

add_question(174,"Policy Features","Medium",
"A policy review helps ensure:",
["Coverage remains appropriate","Premiums disappear","Claims are guaranteed","Rules are removed"],
0,
"Reviews help keep coverage suitable.")

add_question(175,"Policy Features","Easy",
"Insurance coverage should match:",
["Client needs and risks","Random choices","Market rumours","Advisor convenience"],
0,
"Coverage should be based on individual circumstances.")




add_question(176,"Disability Insurance","Medium",
"The definition of disability is important because it:",
["Determines when benefits are payable","Sets investment returns","Changes tax rules","Chooses beneficiaries"],
0,
"The policy definition determines eligibility for benefits.")

add_question(177,"Disability Insurance","Easy",
"Disability insurance is especially important for:",
["People who rely on employment income","Only retired people","Only investors","Only homeowners"],
0,
"Income earners benefit from disability protection.")

add_question(178,"Disability Insurance","Medium",
"Future income protection helps with:",
["Long-term financial security","Investment speculation","Property purchases","Tax avoidance"],
0,
"Protecting income supports financial stability.")

add_question(179,"Health Insurance","Easy",
"Health insurance coverage depends on:",
["The policy contract","Personal preference","Market prices","Agent opinion"],
0,
"Coverage is determined by policy terms.")

add_question(180,"Health Insurance","Medium",
"A health claim may be declined if:",
["The expense is not covered","The client asks politely","The receipt is clear","The premium was paid"],
0,
"Claims must meet coverage requirements.")

add_question(181,"Travel Insurance","Easy",
"Travel insurance protects against:",
["Unexpected events during travel","Guaranteed vacations","Investment changes","Career choices"],
0,
"Travel insurance helps manage travel risks.")

add_question(182,"Travel Insurance","Medium",
"Before travel, clients should confirm:",
["Coverage details and exclusions","Stock prices","Employment benefits only","Mortgage rates"],
0,
"Reviewing coverage prevents misunderstandings.")

add_question(183,"Underwriting","Medium",
"Underwriting information should be:",
["Complete and accurate","Hidden from the insurer","Estimated","Changed later"],
0,
"Accurate information supports proper underwriting.")

add_question(184,"Underwriting","Easy",
"Insurance risk assessment helps determine:",
["Coverage terms","Vacation plans","Employment contracts","Investment returns"],
0,
"Risk assessment determines appropriate policy terms.")

add_question(185,"Underwriting","Medium",
"A health history may affect:",
["Eligibility and premiums","Policy colour","Advisor schedule","Claim forms only"],
0,
"Health information may affect insurance decisions.")

add_question(186,"Claims","Easy",
"Claims are paid when:",
["Policy requirements are satisfied","Anyone requests payment","Premiums stop","Documents are missing"],
0,
"Valid claims are paid according to contract terms.")

add_question(187,"Claims","Medium",
"The insurer may request additional information to:",
["Evaluate a claim","Increase sales","Change the policy owner","Avoid contracts"],
0,
"Additional information helps assess claims.")

add_question(188,"Claims","Easy",
"False information on a claim may:",
["Cause claim problems","Increase benefits","Guarantee approval","Lower premiums"],
0,
"False information can affect claim decisions.")

add_question(189,"Professional Conduct","Medium",
"An advisor should explain:",
["Advantages and limitations of coverage","Only benefits","Only costs","Only commissions"],
0,
"Clients need complete information.")

add_question(190,"Professional Conduct","Easy",
"Ethical insurance advice requires:",
["Honesty and fairness","Pressure selling","Hidden conditions","False promises"],
0,
"Ethical conduct protects clients.")

add_question(191,"Professional Conduct","Medium",
"Client goals should be considered when:",
["Recommending insurance","Setting government rules","Changing laws","Calculating taxes"],
0,
"Recommendations should reflect client objectives.")

add_question(192,"Basics","Easy",
"Insurance helps reduce:",
["Financial uncertainty","All personal expenses","All risks completely","Investment losses"],
0,
"Insurance manages financial consequences of risk.")

add_question(193,"Basics","Medium",
"Risk management includes:",
["Identifying and reducing financial risks","Ignoring problems","Avoiding planning","Removing all contracts"],
0,
"Insurance is one method of managing risk.")

add_question(194,"Policy Features","Easy",
"Policy conditions explain:",
["Rules of the insurance contract","Investment opportunities","Employment benefits","Tax refunds"],
0,
"Conditions describe contract requirements.")

add_question(195,"Policy Features","Medium",
"A policyholder should review coverage when:",
["Life circumstances change","Nothing ever changes","Claims are impossible","Premiums disappear"],
0,
"Changing needs may require coverage adjustments.")

add_question(196,"Premiums","Easy",
"Premium payments are required to:",
["Maintain coverage","Increase claims","Remove exclusions","Change laws"],
0,
"Premiums keep insurance active.")

add_question(197,"Premiums","Medium",
"Premium amounts are influenced by:",
["Risk factors","Favourite colour","Personal opinions","Weather only"],
0,
"Risk factors affect insurance pricing.")

add_question(198,"Basics","Easy",
"The purpose of insurance planning is to:",
["Protect against financial risks","Guarantee wealth","Avoid responsibility","Replace all savings"],
0,
"Insurance planning protects financial security.")

add_question(199,"Basics","Medium",
"Good insurance decisions require:",
["Understanding needs and coverage","Following rumours","Choosing randomly","Ignoring exclusions"],
0,
"Good decisions require informed choices.")

add_question(200,"Basics","Medium",
"The best insurance recommendation is one that:",
["Fits the client's needs and circumstances","Has the highest commission","Costs the most","Is identical for everyone"],
0,
"Suitable recommendations are based on the client's situation.")


# QUESTIONS WILL BE INSERTED HERE


with open(output, "w") as f:
    json.dump(questions, f, indent=2)

print("Generated questions:", len(questions))
