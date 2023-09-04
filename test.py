from singleton_books_manager import SingletonBooksManager
from singleton_lending_manager import SingletonLendingManager
from singleton_customer_manager import SingletonCustomersManager
from customer import Customer
from book import Book
from genre import Genre
import random
from database import Database


#custmer_name_list = [['אברהם', 'כהן'], ['שמואל', 'לוי'], ['משה', 'גולדברג'], ['רחל', 'איינשטיין'], ['יעקב', 'רוזנבלום'], ['דבורה', 'יעקובי'], ['אהרון', 'שוורץ'], ['מרים', 'כהנא'], ['דניאל', 'ברק'], ['רבקה', 'מלכיאל'], ['אביגיל', 'שטרן'], ['יוסף', 'אדלר'], ['שרה', 'רוזנברג'], ['יעקבי', 'לוי'], ['מרים', 'כץ'], ['אלישבע', 'גרין'], ['נתן', 'כהנא'], ['אסתר', 'גולדמן'], ['יעקב', 'רובין'], ['מרים', 'שפירא'], ['איתן', 'כהן'], ['אלישבע', 'פרידמן'], ['נתנאל', 'אברמוביץ'], ['אביהוד', 'גליקמן'], ['משה', 'יעקובסון'], ['ברכה', 'רוזנטל'], ['יוחנן', 'כהנא'], ['שרה', 'שוורץ'], ['יעקבי', 'גולדשטיין'], ['מרים', 'רז'], ['יפת', 'רובין'], ['יונתן', 'כהן'], ['שרה', 'רוזנבלט'], ['אלחנן', 'פרידמן'], ['מרים', 'לוי'], ['נתן', 'כהני'], ['תמר', 'ברלין'], ['יצחק', 'גולדברג'], ['שרה', 'יעקובי'], ['יעקבי', 'רוזנברג'], ['מרים', 'כהנמן'], ['נחום', 'גליקמן'], ['יעל', 'שוורץ'], ['יוחנן', 'כהנא'], ['אליהו', 'גליקמן'], ['ברכה', 'רוזנברג'], ['עוזיהו', 'כהן'], ['אביבה', 'שמיר'], ['גדעון', 'פריץ'], ['חיה', 'כהן'], ['אבישג', 'רז'], ['מוטי', 'גרין'], ['שרה', 'יעקובסון'], ['יעקב', 'רוזנברג'], ['רוחמה', 'גולדשטיין'], ['ענת', 'כהן'], ['נעמי', 'לוי'], ['משה', 'רובין'], ['רות', 'פרידמן'], ['אלעזר', 'גרינברג'], ['דינה', 'רז'], ['נועה', 'לוי'], ['חיה', 'כהני'], ['ישראל', 'שפיר'], ['שמעון', 'רובין'], ['יוסי', 'שוורץ'], ['לאה', 'כהנמן'], ['עקיבא', 'גליקמן'], ['נפתלי', 'שוורץ'], ['עוזיהו', 'רוזנברג'], ['אברימי', 'שטרן'], ['מנחם', 'גרין'], ['שירי', 'רוזנבלום'], ['יונתן', 'פרידמן'], ['רינה', 'כהן'], ['אליעזר', 'גליקמן'], ['דניאל', 'רז'], ['נתנאל', 'לוי'], ['תמר', 'כהני'], ['יונתן', 'שפיר'], ['שמואל', 'רובין'], ['ישראל', 'שוורץ'], ['רחל', 'גולדשטיין'], ['עמוס', 'כהן'], ['אביבה', 'שטרן'], ['ישראל', 'גרין'], ['שרה', 'רוזנבלום'], ['יעקב', 'פרידמן'], ['רעות', 'כהן'], ['אלישבע', 'גליקמן'], ['דבורה', 'רז'], ['נתן', 'לוי'], ['יצחק', 'כהני'], ['יצחק', 'שפיר'], ['שרה', 'רובין'], ['יעקבי', 'שוורץ'], ['אליהו', 'כהנמן'], ['נתן', 'גליקמן'], ['רחל', 'שוורץ'], ['טל', 'כהנמן']]

#Creating an instance of SingletonList
books_manager = SingletonBooksManager()
books_library = SingletonLendingManager()
#add lending book random
#books_library.delete_row_in_lending(8)
#books_manager.delete_row_in_books(170)
#books_manager.delete_row_in_books(170)


#update db in the book_list
#books_manager.select_books_list()

#books_manager.book_print_instance()


#add book
#books_manager.add_book(Book(book_name='bereshit', author_name='gud', genre=Genre().documentary, publishing_year=1990, age_restriction=False, number_of_pages=1500))

print()

#books_manager.print_instance()

# Removing an item from the books_list
#books_manager.delete_row_in_books(2)

#books_manager.book_print_instance()

#print(book_catalog)
#books_manager.get_catalog_book()

print()

#books_manager.book_search('Hri Potter')


#add custmers in list

costumers_manager = SingletonCustomersManager()
custmer_name_list = [['אברהם', 'כהן'], ['שמואל', 'לוי'], ['משה', 'גולדברג'], ['רחל', 'איינשטיין'], ['יעקב', 'רוזנבלום'], ['דבורה', 'יעקובי'], ['אהרון', 'שוורץ'], ['מרים', 'כהנא'], ['דניאל', 'ברק'], ['רבקה', 'מלכיאל'], ['אביגיל', 'שטרן'], ['יוסף', 'אדלר'], ['שרה', 'רוזנברג'], ['יעקבי', 'לוי'], ['מרים', 'כץ'], ['אלישבע', 'גרין'], ['נתן', 'כהנא'], ['אסתר', 'גולדמן'], ['יעקב', 'רובין'], ['מרים', 'שפירא'], ['איתן', 'כהן'], ['אלישבע', 'פרידמן'], ['נתנאל', 'אברמוביץ'], ['אביהוד', 'גליקמן'], ['משה', 'יעקובסון'], ['ברכה', 'רוזנטל'], ['יוחנן', 'כהנא'], ['שרה', 'שוורץ'], ['יעקבי', 'גולדשטיין'], ['מרים', 'רז'], ['יפת', 'רובין'], ['יונתן', 'כהן'], ['שרה', 'רוזנבלט'], ['אלחנן', 'פרידמן'], ['מרים', 'לוי'], ['נתן', 'כהני'], ['תמר', 'ברלין'], ['יצחק', 'גולדברג'], ['שרה', 'יעקובי'], ['יעקבי', 'רוזנברג'], ['מרים', 'כהנמן'], ['נחום', 'גליקמן'], ['יעל', 'שוורץ'], ['יוחנן', 'כהנא'], ['אליהו', 'גליקמן'], ['ברכה', 'רוזנברג'], ['עוזיהו', 'כהן'], ['אביבה', 'שמיר'], ['גדעון', 'פריץ'], ['חיה', 'כהן'], ['אבישג', 'רז'], ['מוטי', 'גרין'], ['שרה', 'יעקובסון'], ['יעקב', 'רוזנברג'], ['רוחמה', 'גולדשטיין'], ['ענת', 'כהן'], ['נעמי', 'לוי'], ['משה', 'רובין'], ['רות', 'פרידמן'], ['אלעזר', 'גרינברג'], ['דינה', 'רז'], ['נועה', 'לוי'], ['חיה', 'כהני'], ['ישראל', 'שפיר'], ['שמעון', 'רובין'], ['יוסי', 'שוורץ'], ['לאה', 'כהנמן'], ['עקיבא', 'גליקמן'], ['נפתלי', 'שוורץ'], ['עוזיהו', 'רוזנברג'], ['אברימי', 'שטרן'], ['מנחם', 'גרין'], ['שירי', 'רוזנבלום'], ['יונתן', 'פרידמן'], ['רינה', 'כהן'], ['אליעזר', 'גליקמן'], ['דניאל', 'רז'], ['נתנאל', 'לוי'], ['תמר', 'כהני'], ['יונתן', 'שפיר'], ['שמואל', 'רובין'], ['ישראל', 'שוורץ'], ['רחל', 'גולדשטיין'], ['עמוס', 'כהן'], ['אביבה', 'שטרן'], ['ישראל', 'גרין'], ['שרה', 'רוזנבלום'], ['יעקב', 'פרידמן'], ['רעות', 'כהן'], ['אלישבע', 'גליקמן'], ['דבורה', 'רז'], ['נתן', 'לוי'], ['יצחק', 'כהני'], ['יצחק', 'שפיר'], ['שרה', 'רובין'], ['יעקבי', 'שוורץ'], ['אליהו', 'כהנמן'], ['נתן', 'גליקמן'], ['רחל', 'שוורץ'], ['טל', 'כהנמן']]
true_or_false = [True, False]
for name in custmer_name_list:
    costumers_manager.add_customers(Customer(name[1], name[0], f'{random.randint(2022, 2023)}-{random.randint(1, 5)}-{random.randint(1, 28)}'))


#add book in list
"""
book_name_list = [['הכוח שבתוך עצמך', "דייל קרנג'י"], ['אל תפסיק לחלום', 'פולו קואליו'], ['ים התמרים', "ז'אן מארי אפלטון"], ['עשרים וארבע שעות בחייו של איש', "ג'יימס ג'ויס"], ['סוד השמשון', 'יוסי אגרי'], ['הפרינססה חוקרת', 'אבי פולדר'], ['האיילה והכלב הצהוב', 'מילן קונדרה'], ['משפחת אדמס', 'נתן דרביץ'], ['השודד והמגדל', "ז'אן לה פון"], ['המרד השני', "ג'ורג' אורוול"], ['צלילי השופר', 'שאול בלנק'], ['אהבה עם פרוסות רגליים', 'גבריאל גארסיה מרקס'], ['סיפור על גבר בן איש', 'פיליפ רות'], ['מקור החיים', 'אילן שור'], ['עור וגידים', 'אליעזר בן יהודה'], ['הכירו את הרובוטים', 'איתמר פלג'], ['עץ חיים', "ז'אן ג'ק רוסו"], ['הצלף', 'נעם סמואל'], ['מייקל בומ', 'דן ברוורמן'], ['סיפורה של מלכת השכונה', 'חולדה אלפר'], ['הילד השקוף', "ג'ודית גור"], ['קרחון באבן', 'יעל דגן'], ['הספר של הטיטאנים', 'יונתן ספירו'], ['סבא הגדול', 'יהודית קורין'], ['הספר שלי', 'דפנה פרז'], ['המעשה בשומריה', 'דוד גרוסמן'], ['חתולים ממלחמת הכוכבים', 'נגה רובין'], ['איש החופש', 'נלסון מנדלה'], ['סיפורה של חיה', 'אהוד בזלאל'], ['הקשר האובליסקי', 'ישראל ישכיל'], ['הכלבה שהתקשרה עם חתול', 'ארקדי דושין'], ['עידן הזהב', 'דורית רבין'], ['כביש החיים', 'אילן שרון'], ['החברים של אמה', 'אילת אלקיים'], ['נכון להיום', 'אברהם ב. יהושע'], ['הילד המרגיש', 'טום וולס'], ['דימויים', 'יהודה עמיחי'], ['משחקי הכחול', 'חגי בן עוזיאל'], ['אסטרואיד 433', 'אברהם בן יהושע'], ['הניצוץ', 'יעקב גלילי'], ['כך יעשה לך חסד', "יפה ד'אהאן"], ['משא ומתן', 'שאול טחולקה'], ['העץ השני', 'ניל גיימן'], ['מאבק למרותו', 'סמואל ברייטמן'], ['שוקולד', 'יעקב שביט'], ['כחול ואדום', 'משה שמיר'], ['מאהבה עד הקצה', 'שושנה ברנד'], ['הניסיון הזה', 'משה צבי זגילבום'], ['הערב של הסטודנטים', 'עמוס עוז'], ['הילד והמחשב', 'עמנואל ארביב'], ['כולם אומרים אהבה', 'אהוד בזלאל'], ['מיסתורי חדר האמנים', 'אהוד אזנב'], ['הכלב של אודסה', "ג'ון גריישם"], ['תאומים ללא רוח', 'אהרון אפלטון'], ['הילד שהתעורר', 'אהרון אפלטון'], ['הבחורה שזהרה בחלומה', 'אסתר רבין'], ['סיפורה של החצובה', 'אהוד בזלאל'], ['סודות בית המקרא', 'יצחק נבון'], ['מאורעות בסדר פריז', 'יוסי אגרי'], ['מחזמרי עולם', 'גבריאל פיל'], ['תותח כתב תיכון', 'עמוס עוז'], ['הכלבה המדבבת', 'מילן קונדרה'], ['שארית היום', 'איתן בר-ילן'], ['גן הפעמונים', 'דורית רבין'], ['הנערה עם חולצת נצח', 'יעל דגן'], ['עוגן במים', 'דבורה בואנו'], ['ספר התורה הקטן', 'עמוס עוז'], ['ירידה למציאות', 'אהוד בזלאל'], ['סיפור על חתול', 'אהוד בזלאל'], ['איפה המקום שלי', "ג'ודית גור"], ['סיפורו של נפטר', 'אליעזר בן יהודה'], ['הילד שהיה בחוץ', 'עוזי יוגב'], ['סיפורים קצרים לגרסאת ילדים', 'איתמר פלג'], ['רחל מאחרת', 'שלום יעקב אברמוביץ'], ['הילדה שהייתה שם', 'חיים בהרייר'], ['מסע לחוף הקרח', 'נעמי רב'], ['הסוד של אורקה', 'יעל דגן'], ['הכרך השמיני', 'פול קרסקו'], ["אורח במלון ריצ'מון", 'אהוד בזלאל'], ['סיפור חייו', 'אהרון אפלטון'], ['הרפתקאות מאולפן הסרטים', 'אהוד בזלאל'], ['האיש שבדלת', 'נעמי רב'], ['סיפורה של רחל', 'אהוד בזלאל'], ['תחתיות הבטנה', 'שמעון פרס'], ['כחול ולבן', 'גיל כהן'], ['עזרא והמשפחה', 'יעקב שביט'], ['הילדה שבמראה', 'עמוס עוז'], ['הגבר שהביא אותה לגן', 'יעל דגן'], ['סיפורה של רינה', 'אהוד בזלאל'], ['השוטר הקטן', 'יהושע קנפפיל'], ['אפריקה', "דוד וולפוביץ'"], ['סיפור על חתול וכלב', 'אהוד בזלאל'], ["משפחת הקרושוביצ'ים", 'עמוס עוז'], ['הכיכר האחרונה', 'איתמר פלג'], ['סיפורה של הפעמון', 'אהוד בזלאל'], ['הילד הנסתר', 'שאול ולנציה'], ['מותה של גברת ברל', 'ישראל הרץ'], ['כחול וסגול', 'משה שמיר'], ['רקוברב', 'יוסף נחמיאס'], ['הילדה שבעה מערכות', 'עמוס עוז'], ['מאה שנות שמחה', 'יוסי קלנר'], ['חמישים הצלילים הגדולים', 'גבריאל גרסיה מרקס'], ['האי המפורסם', 'ארתור גורן'], ['תפילה לירח', 'פאולו קואליו'], ['דברים שלא נאמרו', 'חרם שטרנברג'], ['סיפור פשוט', 'סידני שלדון'], ['עץ הידע', 'קרישנמורטי'], ['האדריכל השולט', 'איילת זרחי'], ['אהבה בזמני רעבון', 'גבריאל גארסיה'], ['התושב הסמרטוט', 'אירנה פרידמן'], ['ילדה בסלע', 'עגנון דורי'], ['אי האוצרות', 'רוברט לואיס סטיבנסון'], ['עולם חדש', 'אלדוס הקסלי'], ['מאה שנות שקט', 'גבריאל גרסיה מרקס'], ['הבית הקטן בקצה העיר', 'אורנה אייכן'], ['מבוכה בזמן', 'מריאן קיין'], ['אי המולדת', 'גאבריאל גרסיה מרקס'], ['ספר החיים', "ז'וזף רוטסטיין"], ['מפגשים מסוכנים', "ג'ון לה קארר"], ['העצמאות', 'חיים חרמון'], ['יומנו של אנה פרנק', 'אנה פרנק'], ['פיליפ רות', 'גיא סטינגל'], ['רחוב האנגלים', 'נגה בלנק'], ['מלחמה ושלום', 'לאה גולדברג'], ['סיפור על דינוזואור', 'מארק טווין'], ['סדרה תפוח', 'אפרים קישון'], ['תמונת משפחה', 'אברהם ב. יהושע'], ['שודדי הים', 'דניאל דפו'], ['עורך דין קרוב', 'גרישם כהן'], ['יומן אנה פרנק', 'אנה פרנק'], ['הקונצרטו השני', 'אנטואן חן'], ['סיפור על פחד', 'גבריאל גרסיה מרקס'], ['אי הסקרנות', "אגת'ה כריסטי"], ['סוסים אחרים', 'אורנה גרינפלד'], ['האם יש חיים במעבר', 'איילת וייזל'], ['דירה בפריז', 'אורנה מנצור'], ['סיפור על שובבים', 'גבריאל גרסיה מרקס'], ['קריאה בספר', 'דורית רביניאן'], ['יומן אדריכל', 'אילן בנצור'], ['ספר הירח', 'גבריאל גרסיה מרקס'], ['האי המסתורי', "ג'ולס ורן"], ['אני, רובוט', 'איזק אזימוב'], ['תרבות אגוזים', 'שירי ארבל'], ['מידבר בערבית', 'רבקה נטל'], ['היד של אדון כבוד', "ג'ון פול סרטר"], ['אבני המגן', 'ראשד ורדי'], ['דירת הדלפק', 'שולמית לוי'], ['הכסא הגורלי', 'רפאל דהן'], ['יומן אנטואן', 'אנטואן דה סנט-אכזופרי'], ['גלידת תותים', 'אריה פינקוביץ'], ['אהובת רופא', 'רחל והודיה כהן'], ['האי הנסתר', "ז'ול ורן"], ['קיץ בשירות האוכלוסין', 'אסף גבילו'], ['הספר השביעי', 'לילה נמצאת'], ['ספר התודעה', 'יוסף זבל'], ['אהבה בימי הקולוניאליזם', 'אברהם בן יוסף'], ['חיפוש אחר האור', "ג'ון גרישם"], ['דרך חורף', 'גליה פרץ'], ['סיפור על פסטורליה', 'גבריאל גרסיה מרקס'], ['יומן אדם ואישה', 'אילן גולדן'], ['תפילה לים', 'דורית רביניאן'], ['סיפור על חצות הלילה', 'גבריאל גרסיה מרקס'], ['האי הקטן', "ג'ולס ורן"], ['אי הסוד', 'רומן שפירא'], ['עונות הנישואים', 'פדריק בקמן'], ['הארי פוטר והאבן הפילוסופלית', "ג'י. קי. רולינג"], ['מסע בשפת האדמה', 'אילן שחר'], ['סיפור על מלאך', 'גבריאל גרסיה מרקס'], ['ספר המשפחה', 'יגאל אלון'], ['הבית של עולם', 'ניל גיימן'], ['ספר החורף', 'גבריאל גרסיה מרקס'], ['הסיפור של רקדן', 'אמוז עוז'], ['יומן איש רע', "ג'ון סטיינבק"], ['קרב ושלום', 'משה דיין'], ['הבית שבקרס', 'גבריאל גרסיה מרקס'], ['אליס בארץ הפלאות', 'לואיס קארול'], ['דירת התיקים', 'גיא סטינגל'], ['הילד שנמלט', 'גיא סטינגל'], ['סיפור על חלומות', 'גבריאל גרסיה מרקס'], ['מועדון הספר', 'אירית פיז'], ['האי הגדול', "ג'ולס ורן"], ['אהבה בזמן קולר', 'גבריאל גרסיה מרקס'], ['סיפור על ילדים', 'גבריאל גרסיה מרקס'], ['תפילה לקיץ', 'אלה שפיגלמן'], ['המיטה בעמדה מאונטרופית', 'איילת פרץ'], ['אודיסיאה', 'הומרוס'], ['הסיפור של בוב', 'אילן שחר'], ['סיפור על מסגרת', 'גבריאל גרסיה מרקס'], ['יומן איש אמן', 'אנריקה קולינה'], ['גיבורים', 'אביגדור הרן'], ['המלך האחרון', 'גיא סטינגל'], ['ילדה למכירה', 'גבריאל גרסיה מרקס'], ['רכבת לדרקון', 'נגה בלנק'], ['דירה בסן פרנסיסקו', 'שולמית לוי'], ['סיפור על אהבה', 'גבריאל גרסיה מרקס'], ['תפילה לחמישה', 'גבריאל גרסיה מרקס'], ['הבית של המשפחה', 'אפרים קישון'], ['ספר המלחמה', 'אברהם בן יוסף'], ['מעגל האש', 'רוחמה המן'], ['סיפור על אושר', 'גבריאל גרסיה מרקס'], ['עורך דין בלבן', 'אילה הלפרין'], ['הקופסה האדומה', 'יוסי גולד'], ['סיפורי חיים', 'רחל יעקבסון'], ['עידו והשולחן המכשיר', 'רותי אילון'], ['מרקוס הבועה', 'דפנה פרז'], ['סיפורי הילדות', 'רותי גוזלן'], ['דודו והחברים הקטנים', 'גיא שלמה'], ['פעם היה ילד', 'דניאלה סמיט'], ['הקופסא הסודית', 'ריקי נוביק'], ['חיות הגן המופלא', 'אלה ברקאי'], ['סיפורי המים', 'אביבה רביב'], ['מסע בין העולמות', 'אביגיל אורון'], ['גידול בגידול', 'טלי ברוכר'], ['המילה האחרונה', 'נועה קירשנבאום'], ['החלום הכחול', 'אירית גלילי'], ['הילד שאיבד את הצחוק', 'רותי קליין'], ['סיפורים לילדים', 'גליה משה'], ['תותי והגן הקסום', 'מאיה דור'], ['הפרופסור והקרנבל', 'דניאל ספיר'], ['פיטר והמקום הסודי', 'רונית גולדברג'], ['סיפורי החיות', 'רווית אברהם'], ['המילה האחרונה', 'ענבל נמיר'], ['גוגו והאריות', 'אסתר גילון'], ['סיפורי המדבר', 'נועה ארזי'], ['עין האי', 'ספיר שחם'], ['דורון והספר הכחול', 'טל כץ'], ['סיפורי העצים', 'רינת חיים'], ['המלכים הקטנים', 'אלעדה שבירו'], ['חברים בסיכון', 'רותי גרינברג'], ['סיפורי השלג', 'שושנה חזן'], ['עזרא והספר המכותב', 'עדי חלף'], ['הילד הקטן ביער', 'מיה רון'], ['המכתב המופלא', 'יעל יוחננוביץ'], ['סיפורים מסביב לעולם', 'תמר דרזי'], ['המפתח האבוד', 'אילה הרצל'], ["ג'קי והמכתב הקסום", 'אביבה רגב'], ['סיפורי המדבר', 'שקד אבישג'], ['גדי והמפתח הקסום', "מרים אברג'יל"], ['חוה והפרחים הקסומים', 'יעל אפרתי'], ['סיפורים מהים', 'נירית דרורי'], ['ניקי והסיפורים הקטנים', 'שירה ברקאי'], ['הילדה שהפכה לקסם', 'ענת מימון'], ['סיפורי השמים', 'נטע יעקבי'], ['מטילדה לפרנסה', 'רבקה יעל'], ['יהלום והחברים הקטנים', 'מיה גורביץ'], ['סיפורי הצמחים', 'גלית אור'], ['ניקו והמילה הנשכחת', "אלכסנדרה סטורצ'נקו"], ['המפתח הכסף', 'אפרת אלון'], ['הילדה הכחולה', 'אלעדה הרצל'], ['סיפורים מהחוף', 'עדי רון'], ['הגיבור הסודי', 'רועי ברוך'], ['סיפור על אהבה', 'איתמר ויצמן'], ['הדיקטטור האחרון', 'יעל נבו'], ['כשהאהבה עברה חוף', 'שרה לוי-אבקסיס'], ['מאחורי הקיר', 'יעל גוזלן'], ['הסודות שבנינו', 'אילת בוכבינדר'], ['סיפורי האושר', 'רחל שלו'], ['אם תרצו', 'דורית רביניאן'], ['תקווה ותעשייה', 'משה זינגר'], ['פוליטיקה על גבי קרח', 'עודד זכאי'], ['הילדה שעמדה בפתח', 'רועי קסטיאל'], ['סיפורים מארבע רוחות', 'מתי זנדברג'], ['מעין החיים', 'מיכל זוהר'], ['עשרים עשרה', 'אפרים סבאג'], ['סיפור על עץ', 'איתמר שיניל'], ['האיש שקיבל הכל', 'רון סופר'], ['ילדה בשטן', 'שרה ליפסקר'], ['האח הקטן', 'ניצן וילנסקי'], ['חייל החירות', 'אורית סלע'], ['עיניים פתוחות', 'עמוס עוז'], ['מישהו בדרכים', 'שרה שביט'], ['סיפורי הלילה', 'ירדן יצחק'], ['המילה האחרונה', 'מרים קורן'], ['תפילה לילדה', 'אילה אור'], ['חידת התופים', 'רוני פורטי'], ['המסע האחרון', 'דניאל כהן'], ['חתול החלב', 'נועה לילין'], ['סיפור על חתימה', "שיר רובינוביץ'"], ['אבא עם כינויים', 'מירב שור'], ['האיש המיוחד', 'יעל דוד'], ['מעל הר ומתחת למים', 'דורית ריבלין'], ['חולמים על רגעים', 'ענבל ארזי'], ['הילדה האבודה', 'אילת כהן'], ['סיפורים למחר', 'יובל ברוח'], ['פיל בגינה', 'רונה בן דוד'], ['כלבה בלתי נראית', 'נטע אורן'], ['הילד והשעון המרתק', 'דנה שרון'], ['סיפורי נוער', 'תמר אילון'], ['המילה המופלאה', 'עמליה אמיר'], ['חיים בימי הקורונה', 'יעל אזולאי'], ['הקסם שבין השורשים', 'אביבית בר'], ['סיפורי גאונים', 'רותי עוז'], ['תפקיד מול כוכב', 'אלה יעקבי'], ['מהיר ומעצבן', 'רעות כהן'], ['פעם בחיים', 'נועה שלו'], ['סיפורים למתבגרים', 'אורית אבני'], ['המחתרת הסודית', 'דניאל קליאן'], ['גיבור החלומות', 'אורן נחום'], ['הבחירה הכחולה', 'יעל קצב'], ['סיפורים מהעבר', 'ירדן גלבוע'], ['דרך החלב', 'רחל חובה'], ['סיפור על אהבה', 'נועה יעקובי'], ['המילים הקסומות', 'יעל נגר'], ['האישה הבלתי נראית', 'מיה גלעד'], ['העיר המאובנת', 'רועי ברזילי'], ['חתול בית הספר', 'תמר לוי'], ['סיפורים מהמרקום', 'אור עמיר'], ['ילדה בלעדית', 'שרה שפירא'], ['אהבה למבוגרים', 'רותי פרלמן'], ['מאחורי הקיר', 'ניצן סוכניק'], ['סיפורי הים התיכון', 'יעל גולדריך'], ['האיש שלא ידע כישוף', 'עידן ירושלמי'], ['פעם בשבת', 'אורלי נויברגר'], ['חיים כמו חופש', 'נועה קצין'], ['סיפורים לקיץ', 'שירה ארנון'], ['עין בין העיר', 'דורית אשל'], ['סיפורים מהמרתף', 'רפאל לוי'], ['ילד בפנים', 'נילי בן צידון'], ['תחפושות בלתי נראות', 'מיה גורביץ'], ['הבחירה המאומצת', 'אילת רותם'], ['סיפורי המדבר', 'יעל בן דוד'], ['מילים מתוך הלב', 'תמר אבישי'], ['הפעם האחרונה', 'רוני קירסטי'], ['חולות מתחת לגשר', 'אלעד פרץ'], ['סיפורי הגבעה', 'שקד פרץ'], ['האישה שבתוכך', 'מיה רן'], ['סיפור על זהב', 'נועה דגן'], ['המילה האחרונה', 'אדל גינץ'], ['ילדה בלעדית', 'רחל נמרוד'], ['תיק החורף', 'דניאל שטרן'], ['חתול בחלום', 'תמר שפיר'], ['סיפורים מהבור', 'יעל לוי'], ['הילדה הנסתרת', 'מיה רוזן'], ['אהבה במבט ראשון', 'רותי קליין'], ['מעבר לגבולות', 'ניצן נחמני'], ['סיפורים מאחורי הפרוזה', 'עמית שביט'], ['הסיפור של אחד', 'יעל אהרונוביץ'], ['פעם בסתיו', 'אילה קסטיאל'], ['חיים כמו מרץ', 'רעות חזן'], ['סיפורים לנערים', 'תמר רזיאל'], ['עין בין המילים', 'דורית אביב'], ['סיפורים ממרכז העיר', 'רפאל דוידוב'], ['ילדים בלתי נראים', 'נירית בן חן'], ['תחתונים על החברה', 'מיה לוזון'], ['הבחירה האובדת', 'אורית ברקת'], ['סיפורים מהפארק', 'יעל ברזילי'], ['מילים מעבר לשפת המים', 'דיקלה כהן'], ['הפעם השנייה', 'רותי קרני'], ['חורבן הקיץ', 'אלעד דרורי'], ['סיפורי הנחל', 'שירי קפלן'], ['הדרך אל האור', 'מיה שטרן'], ['סיפור על אהבה', 'נועה אברמוביץ'], ['הפנקס האחרון', 'אביבית כהן'], ['ילדה בלתי נשכחת', 'רחל עזרא'], ['תמיד יחד', 'דניאל לוי'], ['חתול במציאות', 'תמר פרידמן'], ['סיפורים מהטבע', 'יעל שחורי'], ['הילדה הנעלמת', 'מיה אדלר'], ['אהבה במבט ראשון', 'רותם קליין'], ['מעבר לקיר', 'נורית גרוס'], ['סיפורים ממעבר המסכים', 'עמית גבע'], ['הסיפור שלך', 'יעל כהנא'], ['פעם באביב', 'אילה שלג'], ['חיים כמו רץ', 'רעות רובינשטיין'], ['סיפורים לנערות', 'תמר פרץ'], ['עין בין המילים', 'דורית אביבי'], ['סיפורים מתוך הסוד', 'רפאל לוין'], ['ילדים בגנים', 'נילי גולדברג'], ['תחתונים בפנים', 'מיה לביא'], ['הבחירה האבודה', 'אורית בראון'], ['סיפורים מהשדה', 'יעל ברינר'], ['מילים מעבר לשפה', 'דיקלה כהן'], ['הפעם השלישית', 'רותי גולן'], ['חורבן הקיץ', 'אלעד דורון'], ['סיפורי הנחל', 'שירה קופלן']]
genre_list = a = ['actiom', 'tension', 'horror', 'comedy', 'drama', 'israeli', 'classic', 'children', 'documentary']
true_or_false = [True, False]
for name in book_name_list:
    books_manager.add_book(Book(book_name=name[0], author_name=name[1], genre=random.choice(genre_list), publishing_year=random.randint(1980, 2022), age_restriction=random.choice(true_or_false), number_of_pages=random.randint(50, 700)))
"""

# insert books random
"""
db1 = Database('library')
books = db1.select('books')
for i in range(500):
    for name in random.choices(books):
        print(name)
        books_manager.add_book(Book(book_name=name[1], author_name=name[2], genre=name[3], publishing_year=name[4], age_restriction=name[5], number_of_pages=name[6]))
"""

#To remove all rows in SQLite

"""
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Delete all rows from the table
cursor.execute('DELETE FROM library')

# Commit the changes
conn.commit()

# Close the connection
conn.close()
"""

#add column in db
"""
import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

alter_query = "ALTER TABLE library ADD COLUMN status data_type"
cursor.execute(alter_query)

conn.commit()
conn.close()
"""

#create table db and insert of library
"""
import sqlite3

con = sqlite3.connect("library.db")

cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS library (
            id INTEGER PRIMARY KEY,
            book_id INTEGER,
            costumer_id INTEGER)''')
con.commit()  # Remember to commit the transaction after executing INSERT.
cur.close()
con.close()
"""

#create table db and insert of books and of costumers
"""
import sqlite3
con = sqlite3.connect("library.db")

cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            book_name TEXT,
            author_name TEXT,
            genre TEXT,
            publishing_year INTEGER,
            age_restriction TEXT,
            number_of_pages INTEGER,
            available TEXT)''')
            
books_data = [
    ('Harry Potter1', 'yosi', 'action', 1982, True, 350, True),
    ('Harry Potter2', 'moti', 'comedy', 1992, False, 150, True),
    ('Harry Potter3', 'hani', 'action', 2000, True, 700, True),
    ('Harry Potter4', 'yosi', 'action', 1982, True, 350, True),
    ('Harry Potter5', 'moti', 'comedy', 1992, False, 150, True),
    ('Harry Potter6', 'hani', 'action', 2000, True, 700, True),
    ('Harry Potter1', 'yosi', 'action', 1982, True, 350, True),
    ('Harry Potter2', 'moti', 'comedy', 1992, False, 150, True),
    ('Harry Potter3', 'hani', 'action', 2000, True, 700, True),
]


cur.executemany("INSERT INTO books (book_name, author_name, genre, publishing_year, age_restriction, number_of_pages, available) VALUES(?, ?, ?, ?, ?, ?, ?)", books_data)
con.commit()  # Remember to commit the transaction after executing INSERT.


cur.execute('''CREATE TABLE IF NOT EXISTS costumers (
            id INTEGER PRIMARY KEY,
            costumer_name TEXT,
            subscription_information TEXT,
            books_he_has INTEGER)''')


costumers_data = [
    ( "Mendi", '1983-11-29', 0),
    ( "Mechi", '1983-11-29', 2),
    ( "Malci", '1983-11-29', 3),
    ( "Menachem", '1983-11-29', 1),
    ( "itamar", '1983-11-29', 2),
    ( "yair", '1983-11-29', 1),
]

cur.executemany("INSERT INTO costumers (costumer_name, subscription_information, books_he_has) VALUES(?, ?, ?)", costumers_data)
con.commit()  # Remember to commit the transaction after executing INSERT.

for row in cur.execute("SELECT id, book_name, genre, publishing_year FROM books ORDER BY book_name"):
    print(row)

print()

for row in cur.execute("SELECT id, costumer_name, subscription_information, books_he_has FROM costumers ORDER BY costumer_name"):
    print(row)

"""

#class books_manager old
"""
from book import Book

class BooksManager:

    def __init__(self):
        self.book_list = []

    def get_list_book(self):
        return self.book_list

    def add_book(self, book_id: Book):
        self.book_list.append(book_id)

    def del_book(self, book_id :str):
        for book in self.book_list:
            if book.book_id == book_id:
                self.book_list.remove(book)


    def get_catalog_book(self):
        catalog = []
        for book in self.book_list:
            catalog.append(
                f'book_name: {book.book_name}   genre: {book.genre}   author_name: {book.author_name}   number_of_pages: {str(book.number_of_pages)}   publishing_year: {str(book.publishing_year)}   age_restriction: {str(book.age_restriction)}')
        catalog = set(catalog)
        return catalog

    def book_search(self, book_name : str):
        for book in self.book_list:
            if book_name == book.book_name:
                print(book.book_name, book.book_id)
                return
        print('The book does not exist')
        return

"""

#class CostumerManager old
"""
from costumer import Costumer


class CostumerManager:

    def __init__(self):
        self._costumers_list = []

    def add_costumer(self, costumer: Costumer):
        self._costumers_list.append(costumer)

    def del_costumer(self, costumer_id: str):
        for costumer in self._costumers_list:
            if costumer.costumer_id == costumer_id:
                self._costumers_list.remove(costumer)

    def update_subscription(self, costumer_id, date):
        for costumer in self._costumers_list:
            if costumer.costumer_id == costumer_id:
                costumer.date_of_description = date
"""

#exmple class singelton
"""
class SingletonList:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
            cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self):
        if not self.__initialized:
            self.__list = []
            self.__initialized = True

    def get_list(self):
        return self.__list

    def add_item(self, item):
        self.__list.append(item)

    def remove_item(self, item):
        if item in self.__list:
            self.__list.remove(item)


# Creating an instance of SingletonList
list_instance = SingletonList()

# Adding items to the list
list_instance.add_item('apple')
list_instance.add_item('banana')
list_instance.add_item('orange')

# Accessing the list
my_list = list_instance.get_list()
print(my_list)  # Output: ['apple', 'banana', 'orange']

# Removing an item from the list
list_instance.remove_item('banana')

print(my_list)  # Output: ['apple', 'orange']

"""