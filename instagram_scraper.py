import json
import requests
import copy
from base64 import b64encode
from fake_headers import Headers


class InstagramScraper:
    @staticmethod
    def __build_param(username):
        params = {
            'username': username,
        }
        return params

    @staticmethod
    def __build_headers(username):
        return {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'referer': f'https://www.instagram.com/{username}/',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': Headers().generate()['User-Agent'],
            'x-asbd-id': '198387',
            'x-csrftoken': 'VUm8uVUz0h2Y2CO1SwGgVAG3jQixNBmg',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'x-requested-with': 'XMLHttpRequest',
        }

    @staticmethod
    def __make_request(params, headers):
        INSTAGRAM_API_LINK = 'https://www.instagram.com/api/v1/users/web_profile_info/'
        return requests.get(INSTAGRAM_API_LINK, headers=headers, params=params)

    @staticmethod
    def scrape(username):
        try:
            headers = InstagramScraper.__build_headers(username)
            params = InstagramScraper.__build_param(username)
            response = InstagramScraper.__make_request(headers=headers, params=params)

            HTTP_OK = 200
            if response.status_code == HTTP_OK:
                return response.json()['data']['user']
            else:
                print('Error : ', response.status_code, response.text)
        except Exception as ex:
            print(ex)


class InstagramUser:
    def __init__(self, username):
        self.__username = username
        self.__scraped_data = InstagramScraper.scrape(username)
        self.__posts = [
                        {
                            "imageURL" : post["node"]["display_url"],
                            "description" : post["node"]["edge_media_to_caption"]["edges"][0]["node"]["text"],
                            "userName" :  "INSTAGRAM__" + username
                        }
                        for post in self.__scraped_data["edge_owner_to_timeline_media"]["edges"]
                        ]

    def get_posts(self):
        return copy.deepcopy(self.__posts)


def get_all_posts(usernames):
    posts = [{'imageURL': 'https://instagram.ftlv1-1.fna.fbcdn.net/v/t39.30808-6/440779492_18337553713142767_7263727868140578717_n.jpg?stp=dst-jpg_e15&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=107&_nc_ohc=p6KSNdcZdCcQ7kNvgHClLH0&edm=AOQ1c0wAAAAA&ccb=7-5&oh=00_AYCCTp_7NCtiZWuirmuSSdI5kxhrDYD_oHsE_8BF68adjg&oe=66545039&_nc_sid=8b3546', 'description': 'חג העצמאות השנה מחייב אותנו לקיים את צוואתם של אלפי הנספים שהצטרפו לרשימה.. עצב גדול שהקושי עצום אבל לא נשכח כי במותם ציוו לנו חיים.\nב”ה אנחנו כאן בארצנו 🇮🇱\nגאים השנה בכל החיילים וכוחות הבטחון, המילואימניקים האזרחים שקפצו בצו השעה, המשפחות שהקדישו את יקריהם לתקופה לא מבוטלת כדי שנוכל לקום לעוד יום של שליחות ולהמשיך לחזק את העורף בחברה הישראלית.\nשנזכה להיות עם חופשי בארצנו, ללא חשש ושיבוא שלום עלינו - אמן !\nחג עצמאות שמח ! 💙🇮🇱💙', 'userName': 'INSTAGRAM__aguda.sherut'}, {'imageURL': 'https://instagram.ftlv1-1.fna.fbcdn.net/v/t39.30808-6/424728435_18337516486142767_5148191010189697167_n.jpg?stp=dst-jpg_e15&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=107&_nc_ohc=OWYVwk0OXrUQ7kNvgEm1lCn&edm=AOQ1c0wAAAAA&ccb=7-5&oh=00_AYB2wmQXLs4J0qyrzUpPVV7N9_wt8NsDAC3bW6YrvhOvVA&oe=6654768C&_nc_sid=8b3546', 'description': 'יזכור 🕯\nסמ"ר יוסף אביטבול ז"ל\nיום שבת ה-12.08.06, י"ח באב\nנפל במלחמת לבנון השנייה\nאחיה של תמר אביטבול מתנדבת באגודה בהדסה עין כרם❤️\u200d\n\nשבוע לפני התקרית בה נהרג סמל יוסי אביטבול, השתתף במבצע בו נפצע ברגלו ופונה לבית החולים "זיו" שבצפת.\nהוא אושפז שם ליום אחד והתעקש לחזור ליחידתו מיד ולהילחם בחזית לצד חבריו.\n\nביום שבת ה-12.08.06, י"ח באב, נהרג סמל יוסי יחד עם חייל נוסף, חברו ליחידה, בתאונה מבצעית, כאשר טנק ישראלי דרס את שניהם בטעות בכפר חדת\'ה שבגזרה המרכזית בדרום לבנון.\nסמל יוסי אבוטבול היה אמור לחגוג את יום הולדתו העשרים חמישה ימים לאחר שנפל בקרב.\nהוא נטמן למחרת, בבית העלמין הצבאי בעפולה, על רקע האזעקות הרבות שנשמעו באותה שעה.\nאך למרות נפילות הפגזים באזור, מאות ליווהו בדרכו האחרונה.\nהותיר הורים ושבעה אחים ואחיות: אסתר-הודיה, אשר, מעיין, אוריה, יונתן תמר ומשה. \nיוסי הוא האח הבכור מבין שמונת האחים והאחיות.\nעל כן תמיד דאג להם ושימש להם כמודל לחיקוי.\n"הוא היה בחור איכותי, צנוע, ילד אצילי, שקט ונעים הליכות, מסור להוריו ונערץ על אחיו ואחיותיו הקטנים שעבורם הוא היה אבא קטן".\n\nיהי זכרו ברוך💔', 'userName': 'INSTAGRAM__aguda.sherut'}, {'imageURL': 'https://instagram.ftlv1-1.fna.fbcdn.net/v/t39.30808-6/438109617_825040976314644_2710887494672861707_n.jpg?stp=dst-jpg_e15_fr_s1080x1080&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=100&_nc_ohc=AEsqHoEh4LwQ7kNvgEZh6Xv&edm=AOQ1c0wAAAAA&ccb=7-5&oh=00_AYDpSZmEQ8v5ESc9bKgARZh_3h-WrW9mx0CEj8mrlPkqdA&oe=665444D5&_nc_sid=8b3546', 'description': 'יזכור 🕯\nסמ"ר יקיר לוי ז"ל\nשבת שמחת תורה, כ"ב בתשרי 7.10\nמוצב פגה-גבול עזה גדוד 13 גולני\nבן דודה של אוראל מתנדבת באגודה עם המפונים בלביא❤️\u200d\n\nאוראל משתפת...🌹\nיקיר וכמה מחייליו יצאו לסיור לפנות בוקר, מיד שחזרו אל המוצב החל מטח כבד של יירוטים לעבר ישראל ובאותו הזמן הודיעו בקשר על חדירת מחבלים. \nהחיילים במוצב החלו להתייצב בעמדות ולעשות כל שביכולתם למנוע פריצה לבסיס. \nלאחר מספר שעות של קרב קשוח אשר במהלכו לצערנו ספגנו פגיעות רבות וקשות, המחבלים פרצו אל הבסיס והקרב הפך ונהיה קשה יותר ויותר. \nהחיילים התבצרו בתוך חדר האוכל (האזור הממוגן) בעוד שבחוץ המחבלים יורים לתוך החדר רימונים ומטענים כבדים ושורפים את הדלתות מכל כיון, החיילים בפנים החלו להיחנק ולא ידעו מה עליהם לעשות והתחמושת הולכת ונגמרת והם נצורים ללא כל מענה.\n\nחמישה לוחמים 🪖\nיקיר לוי, איתי גליסקו, עידן רז, ליאור עזיזוב ושלו ברנס,\nהחליטו באומץ רב ובתעוזה גדולה לצאת מחדר האוכל תחת אש ולהילחם במחבלים ובאותה העת נפלו כגיבורים אמתיים והצילו את חיי חבריהם ועם ישראל בכלל.💔\nיקיר היה בן דוד מאוד קרוב אליי 🥹\nהיינו מטיילים כל חוה"מ סוכות והוא היה מכיר לנו את כל המקומות הכי יפים וקסומים בארץ, הוא היה מלח הארץ, התנדב במד״א, אהב לטייל ולהכיר את הארץ היפה שלנו ונפל בגבורה רבה על קידושה.\nאנחנו מתגעגעים אליו ומחכים כל יום לביאת המשיח ולתחיית המתים בע״ה🙏🏻', 'userName': 'INSTAGRAM__aguda.sherut'}, {'imageURL': 'https://instagram.ftlv1-1.fna.fbcdn.net/v/t39.30808-6/441873788_18337489015142767_8847363291135684099_n.jpg?stp=dst-jpg_e15&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=107&_nc_ohc=o-QC5bmIbtIQ7kNvgGuMgfv&edm=AOQ1c0wAAAAA&ccb=7-5&oh=00_AYAChwCsfpbT3eHBhSaDnikMQVFIKN_lY1_iHKRgcB-xzw&oe=66546A8B&_nc_sid=8b3546', 'description': 'יזכור 🕯\nאל”מ יצחק בן בשט ז”ל , בן 44 בנופלו\nנפל בקרב שג’אעייה השני, בו פעל כמפקד חפ”ק מח”ט גולני במלחמת חרבות ברזל ⚔\nדודה של נועה אנגלמן מתנדבת כסייעת אחות בפגייה בביה”ח שערי צדק💔\nנועה משתפת...🥺\nיצחק בן בשט הוא דוד שלי או בקיצור בנבה,\nכן עדיין בלשון הווה כי המוות שלו קצת לא נתפס לי.\nליצחק יש שלושה כותרות שמגדירות אותו-\nהוא איש צבא- מה זה אומר? \nיצחק כל הזמן היה קשוח עם הבעת פנים קשוחה, ועם עמידה כזאת של מישהו שעוד רגע מתהפך עליך על הכל. \nאבל הוא לא היה כזה כל הזמן.\nהוא דוד שלי- כמובן זה כבר ידוע לכל שהוא דוד שלי, אבל זה הקטע, הוא לא בנבה אצלי, הוא לא הקצין או סגן אלוף אצלי. \nאצלי הוא פשוט דוד יצחק הרגיל, הפשוט.\nהוא היה מנהיג עם ראש על הכתפיים- יצחק יצא לפנסיה צבאית לפני המלחמה והוא נסע עם המשפחה לטיול ענק בחול, ובשישי לאוקטובר הם חזרו וכבר באותה השבת השחורה הוא נסע לבארי וחילץ משפחות, אפילו נפגשנו עם כמה מהן. \nהוא לא חשב פעמיים וישר נסע, והוא עשה פעולות מטורפות והציל המון אנשים בדרך. \nלמדתי מיצחק מהי מסירות.\nמסירות לעבודה מסירות לאדם מסירות למדינה ולכל עם ישראל, יצחק נפל כשניסה להציל חייל פצוע, וזו לדעתי המסירות נפש הכי גדולה שיש והכי משמעותית שהאדם יכול לעשות.\nככה גם בבית חולים, אני מוכנה להתמסר לעבודה ולהיכנס בה בכל כוחי כי זה הצלת חיי אדם לכל דבר ועניין.\nאני חושבת שכל אחת יכולה לקחת משהו מיצחק על עצמה, לפני שיצחק נפל הוא הקליט לצוות שלו הקלטה שבה נאמר ״אל תכנסו לאווירת נכאים, יש לנו גיבורים בכל הדרגות מכל הסוגים ובכל הגילאים. אין מדינה כזאת! זה החוסן והחוזק שלנו.״\nיצחק הוא הגיבור שלי, גיבור המלחמה שלי.\nועכשיו יום הזיכרון ואני רוצה לבקש ממכם טובה, שימו לב לסביבה שלכם, לאנשים שאתכם, ותנסו לעזור ולהתמסר אליהם כמה שרק תוכלו, כי זה מה שיצחק היה עושה.\nתודה על הזכות לשתף אתכם קצת על יצחקי שלי… \nבשורות טובות לכולנו ולכל עם ישראל ❤ @noaengelman1 @shaare_zedek.il', 'userName': 'INSTAGRAM__aguda.sherut'}, {'imageURL': 'https://instagram.ftlv1-1.fna.fbcdn.net/v/t39.30808-6/438173265_18337402399142767_1473063509634670455_n.jpg?stp=dst-jpg_e15&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=107&_nc_ohc=YXCyTO1MBGMQ7kNvgHCdyGK&edm=AOQ1c0wAAAAA&ccb=7-5&oh=00_AYBkEHPem1cARORWa6sqYQmYqPIUaneJdPsdL9PAT4LZTQ&oe=66544F78&_nc_sid=8b3546', 'description': 'יזכור💔  האגודה להתנדבות מתייחדת עם זכר הנופלים והנופלות במערכות  ישראל🕯️ ועם זכרם של קרובי משפחה שנפלו במלחמת חרבות ברזל⚔️', 'userName': 'INSTAGRAM__aguda.sherut'}, {'imageURL': 'https://instagram.ftlv1-1.fna.fbcdn.net/v/t39.30808-6/440352109_18336726265142767_4596808183557783093_n.jpg?stp=dst-jpg_e15_fr_s1080x1080&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=107&_nc_ohc=Ch4-U1DhnBMQ7kNvgFsalYc&edm=AOQ1c0wAAAAA&ccb=7-5&oh=00_AYBb-tZJzG23zNfDOmFqYVYBFFx2d9wbajJR4mNh93_i-Q&oe=66546FB0&_nc_sid=8b3546', 'description': '🇵במוצאי שבת יצאה משלחת הרשות לפולין 🇮🇱 🇵🇱\nשגית כהן צמח, רכזת במחוז צפון, יחד עם שמונה מתנדבים מדהימים\nשמייצגים אותנו בכבוד רב💪🏻\nהמסע מרגש מחבר ומטלטל יחד...🥹 #משלחתלפולין #אגודהלהתנדבות #עםישראלחי', 'userName': 'INSTAGRAM__aguda.sherut'}, {'imageURL': 'https://instagram.ftlv1-1.fna.fbcdn.net/v/t39.30808-6/438145327_18336371992142767_7538821138746968865_n.jpg?stp=dst-jpg_e15&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=107&_nc_ohc=pWUNjWifDUMQ7kNvgH8F9Xk&edm=AOQ1c0wAAAAA&ccb=7-5&oh=00_AYDEyjRnzeMtQLs_DdBva16U0E5z8Nk80LeJfJzFrj6Zqg&oe=66544D49&_nc_sid=8b3546', 'description': 'האגודה להתנדבות מרכינה ראש לזכר קורבנות השואה💔 \nאנחנו מחזקים את שורדי התופת ואת השותפים לתקומת העם – שעדיין חיים בינינו.  אנו מחבקים אתכם בליבנו ובמחשבותינו🥺', 'userName': 'INSTAGRAM__aguda.sherut'}, {'imageURL': 'https://instagram.ftlv1-1.fna.fbcdn.net/v/t39.30808-6/441856348_18336349957142767_6200183014928462175_n.jpg?stp=dst-jpg_e15&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=107&_nc_ohc=f6CB3tyP0AIQ7kNvgHwAsJm&edm=AOQ1c0wAAAAA&ccb=7-5&oh=00_AYAuXWEYFu6bCc7Gbs4Qxr7zp5NABMPSNPilw6KXKcTzxA&oe=665475C3&_nc_sid=8b3546', 'description': 'אבישג מתנדבת במחלקת חדרי לידה ומיון יולדות👼 בבית חולים הדסה הר הצופים בירושלים🏥,\nלאבישג יש אינטרקציה רבה עם המטופלות במחלקה, כגון לשים מוניטור עוברי, לקחת סימנים וכו’...\nכמו כן היא מתחברת להרבה מהמטופלות ששוהות במיון לזמן קצר ואין דבר שהיא יותר אוהבת מלראות אותן אחרי הלידה עם התינוק הקטן והחדש שלהן😇.\nזוהי סגירת מעגל שמוסיפה הרבה סיפוק ושמחה לתפקיד שלה😊.\nאחת מהחוויות שעברה במהלך השירות-\nמטופלת שזכורה לי מאוד- באחד הימים העמוסים במיון היא הגיעה והפכנו ממש לחברות זאת הייתה אחת המשמרות הכי משוגעות שהיו לי,\nוכל מה שהיא עשתה זה לפתם אותי באוכל ולהעלות לי חיוך כל פעם שראיתי אותה💞.\nיום לאחר מכן הגעתי למשמרת והיא הייתה שם וחיפשה אותי וסיפרה לי על כל מה שעבר עליה כשלא הייתי, וכך גם בהמשך היום היא המשיכה ועדכנה אותי כשנכנסה לחדר לידה והמשכתי לבקר אותה שם עד סוף המשמרת.\nיום למחרת אחת בנות השירות במחלקת היולדות התקשרה אלי וסיפרה לי שיש מטופלת שמבקשת אותי, ברגע שהתפניתי עליתי למחלקה וראיתי שזאת אותה המטופלת שהתחברתי אליה בימים הקודמים לכך -זה היה אחד הרגעים הכי מרגשים בשירות שלי🥹, לראות את המטופלת שכל כך התחברתי אליה וכל כך רצתה כבר ללדת, מחזיקה את התינוקת הקטנה שלה🤱.\nזוהי הזדמנות שלנו להוקיר תודה🙏🏻לכל המתנדבות שלנו שפועלות במחלקות חדרי הלידה ומיון יולדות גאים בכל אחת ואחת מכן, מוקירים אתכן ומלאים הערכה!💙 #יוםהמיילדותהבינלאומי #הדסההרהצופים #אגודהלהתנדבות', 'userName': 'INSTAGRAM__aguda.sherut'}, {'imageURL': 'https://instagram.ftlv1-1.fna.fbcdn.net/v/t39.30808-6/440090694_18335723089142767_2079025703896229975_n.jpg?stp=dst-jpg_e15&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=107&_nc_ohc=OIegZCUktiwQ7kNvgEtU6h1&edm=AOQ1c0wAAAAA&ccb=7-5&oh=00_AYA7hBumO3-XzU0nD-o67QJtlttiiGlKWTWpWQBK29YxoA&oe=66544BB2&_nc_sid=8b3546', 'description': 'חזרה לשגרה נעימה לכולם🌻💙', 'userName': 'INSTAGRAM__aguda.sherut'}, {'imageURL': 'https://instagram.ftlv1-1.fna.fbcdn.net/v/t39.30808-6/439078502_18334606210142767_9119475552446596584_n.jpg?stp=dst-jpg_e15&_nc_ht=instagram.ftlv1-1.fna.fbcdn.net&_nc_cat=107&_nc_ohc=iHPoWk_kGtkQ7kNvgFl3xJk&edm=AOQ1c0wAAAAA&ccb=7-5&oh=00_AYDYFIQQ5ZsYHc0mbIyJ2tAz7PRU94nvDmDKg_R5ElNKNA&oe=665458FB&_nc_sid=8b3546', 'description': 'חג שמח מתנדבים/ות ועובדים יקרים 🥂🌻\nמאחלים לכם חופשה נעימה 💙\n#פסחכשרושמח #האגודהלהתנדבות', 'userName': 'INSTAGRAM__aguda.sherut'}]
    for username in usernames:
        try:
            user = InstagramUser(username)
            posts += user.get_posts()
        except:
            pass

    return posts
