import telebot
from telebot.types import MessageID

bot = telebot.TeleBot("token")

virkey = telebot.types.ReplyKeyboardMarkup()
virkey.row('/пока', '/start', '/язык', '/помощь')

langkey = telebot.types.ReplyKeyboardMarkup()
#langkey.row('/Python', '/C++')

Help = '''Доступный функционал:
start - начать работу
помощь - показываю мой функционал
пока - завершить работу
если напишешь 'да', то я покажу список задач
''' 

task102c = '''
#include <iostream>

using namespace std;

bool IsDigit (char c)
{
    return ((c >= '0') && (c <= '9'));
}

int main ()
{
    char c;
    cin >> c;

    cout << ((IsDigit (c)) ? "yes" : "no");

    return 0;
}
'''
task1023c = '''
#include <iostream>

using namespace std;

int main ()
{
    int n;
    cin >> n;

    for (int i (0); i < n; i++)
    {
        int h;
        cin >> h;

        if (h <= 437)
        {
            cout << "Crash " << i + 1;
            return 0;
        }
    }

    cout << "No crash";

    return 0;
}
'''
task103c = '''
#include <iostream>

using namespace std;

unsigned char ToUpper (char c)
{
    return ((c >= 'a') && (c <= 'z')) ? c - ' ' : c;
}

int main ()
{
    char c;
    cin >> c;

    cout << ToUpper (c);

    return 0;
}
'''
task104c = '''
#include <iostream>

using namespace std;

unsigned char ChangeCase (char c)
{
    if ((c >= 'a') && (c <= 'z'))
    {
        return c - ' ';
    }

    return ((c >= 'A') && (c <= 'Z')) ? c + ' ' : c;
}

int main ()
{
    char c;
    cin >> c;

    cout << ChangeCase (c);

    return 0;
}
'''
task105c = '''
#include <iostream>
#include <string>

using namespace std;

bool Compare (string S1, string S2)
{
    return S1 == S2;
}

int main ()
{
    string s1, s2;
    cin >> s1 >> s2;

    cout << (Compare (s1, s2) ? "yes" : "no");

    return 0;
}
'''
task106c = '''
#include <iostream>
#include <string>

using namespace std;

int main ()
{
	string s;
	getline (cin, s);

	int count (1);
	for (int i = 0; i < s.length(); i++)
	{
		if ((s[i] == ' ') && (s[i - 1] != ' '))
		{
			count++;
		}
	}

	cout << count;

	return 0;
}
'''
task107c = '''
#include <iostream>
#include <string>

using namespace std;

int main ()
{
	string s, maxs ("");

	while (cin >> s)
	{
		if (s.length () > maxs.length ())
		{
			maxs = s;
		}
	}

	cout << maxs << endl << maxs.length ();

	return 0;
}
'''
task108c = '''
#include <iostream>
#include <string>

using namespace std;

int main ()
{
	string s;
	cin >> s;

	bool result (true);
	for (int i = 0; i <= s.length () / 2; i++)
	{
		if (s[i] != s[s.length () - 1 - i])
		{
			result = false;
			break;
		}
	}

	cout << ((result) ? "yes" : "no");

	return 0;
}
'''
task109c = '''
#include <iostream>
#include <string>
#include <set>

using namespace std;

int main ()
{
	string s;
	cin >> s;

	set<char> symbols;
	for (char c : s)
	{
		if (symbols.find (c) != symbols.end ())
		{
			cout << c;
			break;
		}

		symbols.insert (c);
	}

	return 0;
}
'''
task110c = '''
#include <iostream>
#include <string>

using namespace std;

int main ()
{
	string a, b;
	cin >> a >> b;

	cout << ((b.find(a) != string::npos) ? "yes" : "no");

	return 0;
}
'''
task111c = ''' 
#include <iostream>
#include <string>

using namespace std;

int main ()
{
	string dir;
	int a, x (0), y (0);
	while (cin >> dir >> a)
	{
		if (dir == "North")
		{
			y += a;
		} else if (dir == "South")
		{
			y -= a;
		} else
		{
			x += (dir == "East") ? a : -a;
		}
	}

	cout << x << ' ' << y;

	return 0;
}
'''
task111642c = '''
#include <iostream>

using namespace std;

int main ()
{
    int a, b;
    cin >> a >> b;

    cout << a + b;

    return 0;
}
'''
task111660c = '''
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main ()
{
    string n;
    cin >> n;

    sort (n.begin (), n.end ());

    long long nn(stoll (n) * 9);
    int sum (0);
    for (; nn; sum += nn % 10, nn /= 10);

    cout << sum;

    return 0;
}
'''
task111668c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	int a (0);
	for (int d (1); d <= n; d++)
	{
		a += (n % d > 0);
	}

	cout << n - a;

    return 0;
}
'''
task111670c = '''
#include <iostream>

using namespace std;

int main ()
{
	int x, y, z;
	cin >> x >> y >> z;

	if (y < x)
	{
		swap (y, x);
	}
	if (z < y)
	{
		swap (y, z);
	}
	if (y < x)
	{
		swap (y, x);
	}

	cout << x << ' ' << y << ' ' << z;

    return 0;
}
'''
task112c = '''
#include <iostream>
#include <string>

using namespace std;

int main ()
{
	string final (""), s;
	for (; cin >> s; final += s);

	bool result (true);
	for (int i = 0; i <= final.length () / 2; i++)
	{
		if (final[i] != final[final.length () - i - 1])
		{
			result = false;
			break;
		}
	}

	cout << (result ? "yes" : "no");

	return 0;
}
'''
task112145c = '''
#include <iostream>

using namespace std;

int main ()
{
    int a, b, c;
    cin >> a >> b >> c;

    cout.precision (3);
    cout << fixed << a << '+' << b << '+' << c << '=' << a + b + c << endl;
    cout << a << '*' << b << '*' << c << '=' << a * b * c << endl;
    cout << '(' << a << '+' << b << '+' << c << ")/3=" << (a + b + c) / 3.f;

    return 0;
}
'''
task112147c = ''' 
#include <iostream>

using namespace std;

int main ()
{
    float a;
    cin >> a;

    float result (a * a);
    result = result * result * a;

    cout.precision (3);
    cout << fixed << result * result;

    return 0;
}
'''
task112161c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;
	
	if ((n < 1) || (n > 12))
	{
		cout << "NO";
	} else if ((n >= 3) && (n <= 5))
	{
		cout << "spring";
	} else if ((n >= 6) && (n <= 8))
	{
		cout << "summer";
	} else
	{
		cout << (((n >= 9) && (n <= 11)) ? "autumn" : "winter");
	}

	return 0;
}
'''
task112162c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	const int month[] {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
	
	if ((n < 1) || (n > 12))
	{
		cout << 0;
	} else
	{
		cout << month[n - 1];
	}

	return 0;
}
'''
task113c = ''' 
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	int a (1);
	while (a * a <= n)
	{
		cout << a * a << endl;
		a++;
	}

	return 0;
}
'''
task113652c = '''
#include <iostream>

using namespace std;

bool check (int n)
{
	if (n < 1)
	{
		return false;
	} else if (n == 1)
	{
		return true;
	}

	return (check (n - 5) || check (n - 3));
}

int main ()
{
	int n;
	cin >> n;

	cout << ((check (n)) ? "YES" : "NO");

	return 0;
}
'''
task113653c = '''
#include <iostream>

using namespace std;

char getMaxNumber (char* n)
{
	if (n[1] == '\0')
	{
		return n[0];
	}

	char c (getMaxNumber (n + 1));
	return ((c > n[0]) ? c : n[0]);
}

int main ()
{
	char n[1000];
	cin >> n;

	cout << (getMaxNumber (n));

	return 0;
}
'''
task113654c = '''
#include <iostream>

using namespace std;

int getNumberCount (char* n)
{
	if (n[0] == '\0')
	{
		return 0;
	}

	return ((n[0] >= '0') && (n[0] <= '9')) + getNumberCount (n + 1);
}

int main ()
{
	char n[1000];
	cin >> n;

	cout << (getNumberCount (n));

	return 0;
}
'''
task113655c = ''' 
#include <iostream>
#include <string>

using namespace std;

string insertStar (string s)
{
	if (s.length () == 1)
	{
		return s;
	}

	string result ("*" + insertStar (s.substr (1)));
	result.insert (result.begin (), s[0]);
	return result;
}

int main ()
{
	string s;
	cin >> s;

	cout << insertStar (s);

	return 0;
}
'''
task113656c = '''
#include <iostream>
#include <string>

using namespace std;

string insertBrackets (string s)
{
	if (s.length () <= 2)
	{
		return s;
	}

	string result ("(" + insertBrackets (s.substr (1, s.length () - 2)) + ")");
	result.insert (result.begin (), s[0]);
	result.insert (result.end (), s[s.length () - 1]);
	return result;
}

int main ()
{
	string s;
	cin >> s;

	cout << insertBrackets (s);

	return 0;
}
'''
task113657c = '''
#include <iostream>
#include <string>

using namespace std;

string solveTask (string s)
{
	if (s.length () == 0)
	{
		return "";
	}

	string result (solveTask (s.substr (1)));
	result.insert (result.begin (), s[0]);
	result.insert (result.end (), (s[0] == '(') ? ')' : s[0]);
	return result;
}

int main ()
{
	string s;
	cin >> s;

	cout << solveTask (s);

	return 0;
}
'''
task113658c = '''
#include <iostream>
#include <string>

using namespace std;

string archiveString (string s)
{
	if (s.length () == 1)
	{
		return s;
	}
	
	string result ((s.length () > 2) ? archiveString (s.substr (1, s.length () - 2)) : "");
	if (s[0] != s[s.length () - 1])
	{
		result.insert (result.begin (), s[0]);
		result.insert (result.end (), s[s.length () - 1]);
	}
	
	return result;
}

int main ()
{
	string s;
	cin >> s;

	cout << archiveString (s);

	return 0;
}
'''
task113659c = '''
#include <iostream>
#include <vector>
#include <map>

using namespace std;

int visit(map<int, vector<int>> &a, int k);

int visit(map<int, vector<int>> &a, int k) {
    int count = 1;
    if (a.find(k) == a.end()) {
        return count;
    }

    for (int i = 0; i < (int) a[k].size(); ++i) {
        count += visit(a, a[k][i]);
    }

    return count;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n;
    map<int, vector<int>> a;
    for (int i = 0; i < n; ++i) {
        int num;
        int parent;
        cin >> num >> parent;
        if (parent == 0) {
            continue;
        }
        a[parent].push_back(num);
    }
    cin >> k;
    cout << visit(a, k) << endl;

    return 0;
}
'''
task114c = '''
#include <iostream>

using namespace std;

int SumOfDigits (int n)
{
	return (n) ? n % 10 + SumOfDigits (n / 10) : 0;
}

int main ()
{
	int n;
	cin >> n;

	cout << SumOfDigits (n);

	return 0;
}
'''
task115c = '''
#include <iostream>

using namespace std;

int NumberOfZeroes (int n)
{
	return (n) ? (!(n % 10)) + NumberOfZeroes (n / 10) : 0;
}

int main ()
{
	int n;
	cin >> n;

	cout << NumberOfZeroes (n);

	return 0;
}
'''
task116c = '''
#include <iostream>
#include <algorithm>

using namespace std;

int MinDigit (int n)
{
	if (!n)
	{
		return 0;
	}

	int result (9);
	while (n)
	{
		result = min (result, n % 10);
		n /= 10;
	}

	return result;
}

int MaxDigit (int n)
{
	if (!n)
	{
		return 0;
	}

	int result (0);
	while (n)
	{
		result = max (result, n % 10);
		n /= 10;
	}

	return result;
}

int main ()
{
	int n;
	cin >> n;

	cout << MinDigit (n) << ' ' << MaxDigit (n);

	return 0;
}
'''
task117c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	while (n)
	{
		cout << n % 2;
		n /= 2;
	}

	return 0;
}
'''
task11764c = '''
#include <iostream>

using namespace std;

int main ()
{
    int n;
    cin >> n;

    for (int i (0); i < n; i++)
    {
        for (int j (1); j <= i + 1; j++)
        {
            cout << j;
        }

        cout << endl;
    }

    return 0;
}
'''
task118c = '''
#include <iostream>

using namespace std;

int reverse (int n)
{
	int result (0);
	while (n)
	{
		result *= 10;
		result += n % 10;
		n /= 10;
	}

	return result;
}

int main ()
{
	int n;
	cin >> n;

	cout << reverse (n);

	return 0;
}
'''
task119c = '''
#include <iostream>

using namespace std;

int reverse (int n)
{
	int result (0);
	while (n)
	{
		result *= 10;
		result += n % 10;
		n /= 10;
	}

	return result;
}

int main ()
{
	int k;
	cin >> k;

	int result (0);
	for (int i (1); i <= k; i++)
	{
		if (i == reverse (i))
		{
			result++;
		}
	}

	cout << result;

	return 0;
}
'''
task120c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	if (n > 8)
	{
		n = 8;
	}

	float result (1);
	int factorial (1);
	for (int i (1); i <= n; i++)
	{
		factorial *= i;
		result += 1. / factorial;
	}

	cout << result;

	return 0;
}
'''
task121c = '''
#include <iostream>

using namespace std;

int main ()
{
	int a, i;
	cin >> a >> i;

	int mask (0);
	for (int j (0); j < i; j++)
	{
		mask |= 1 << j;
	}

	cout << (a & ~mask);

	return 0;
}
'''
task122c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n, m;
	cin >> n >> m;

	cout << ((1 << n) | (1 << m));

	return 0;
}
'''
task123c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	cout << (1 << n);

	return 0;
}
'''
task124c = '''
#include <iostream>

using namespace std;

int main()
{
	int a, i;
	cin >> a >> i;

	cout << (a | (1 << i));

	return 0;
}
'''
task125c = '''
#include <iostream>

using namespace std;

int main ()
{
	int a, i;
	cin >> a >> i;

	cout << (a ^ (1 << i));

	return 0;
}
'''
task126c = '''
#include <iostream>

using namespace std;

int main ()
{
	int a, i;
	cin >> a >> i;

	cout << (a & ~(1 << i));

	return 0;
}
'''
task127c = '''
#include <iostream>

using namespace std;

int main ()
{
	int a, i;
	cin >> a >> i;

	int mask (0);
	for (int j (0); j < i; j++)
	{
		mask |= 1 << j;
	}

	cout << (a & mask);

	return 0;
}
'''
task128c = '''
#include <iostream>

using namespace std;

int main ()
{
	int a, i;
	cin >> a >> i;

	cout << ((a & (1 << i)) ? 1 : 0);

	return 0;
}
'''
task129c = ''' 
#include <iostream>

using namespace std;

int main ()
{
	int a;
	cin >> a;

	for (int i (7); i >= 0; i--)
	{
		cout << ((a & (1 << i)) ? 1 : 0);
	}

	return 0;
}
'''
task1404c = '''
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct Student
{
	string surname, name, form, birthday;
};

bool compare (Student s1, Student s2)
{
	if (s1.form == s2.form)
	{
		return (s1.surname < s2.surname);
	}

	if (s1.form.length () == s2.form.length ())
	{
		return (s1.form < s2.form);
	}

	return (s1.form.length () < s2.form.length ());
}

int main ()
{
	int n;
	cin >> n;

	vector<Student> students;
	for (int i (0); i < n; i++)
	{
		string surname, name, form, birthday;
		cin >> surname >> name >> form >> birthday;

		students.push_back (Student {surname, name, form, birthday });
	}

	sort (students.begin (), students.end (), compare);

	for (Student s : students)
	{
		cout << s.form << ' ' << s.surname << ' ' << s.name << ' ' << s.birthday << endl;
	}

	return 0;
}
'''
task1415c = '''
#include <iostream>
#include <string>

using namespace std;

int main ()
{
	string s;
	int k;
	cin >> s >> k;

	for (char c : s)
	{
		cout << (char) ('A' + (c - 'A' - k + 26) % 26);
	}

	return 0;
}
'''
task1417c = '''
#include <iostream>
#include <string>

using namespace std;

int main ()
{
	string s;
	int a, b;
	getline (cin, s);
	cin >> a >> b;

	a--;
	b--;
	for (int i = 0; i <= (b - a) / 2; i++)
	{
		swap (s[a + i], s[b - i]);
	}

	cout << s;

	return 0;
}
'''
task1418c = '''
#include <iostream>
#include <set>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	set<int> data;
	for (int i (0); i < n; i++)
	{
		int a;
		cin >> a;
		data.insert (a);
	}

	cout << data.size ();

	return 0;
}
'''
task1421c = ''' 
#include <iostream>
#include <string>

using namespace std;

int main ()
{
	string s;
	getline (cin, s);
	cout << s[0];
	for (int i = 1; i < s.length (); i++)
	{
		if ((s[i] == ' ') && (s[i - 1] == ' '))
		{
			continue;
		}

		cout << s[i];
	}

	return 0;
}
'''
task1430c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	int number (1), count (1);
	for (int i (0); i < n; i++)
	{
		if (!count)
		{
			number++;
			count = number;
		}

		cout << number << ' ';
		count--;
	}

	return 0;
}
'''
task1433c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n, m;
	cin >> n >> m;

	cout << m / n + (m % n > 0);

	return 0;
}
'''
task1435c = '''
#include <iostream>
#include <string>

using namespace std;

bool isCorrectPart (string part)
{
	return ((part.length () > 0) && (atoi (part.c_str ()) <= 255));
}

int main ()
{
	string ip;
	getline (cin, ip);

	int pos;
	while ((pos = ip.find ('.')) != string::npos)
	{
		if (!isCorrectPart (ip.substr (0, pos)))
		{
			cout << 0;
			return 0;
		}

		ip.erase (0, pos + 1);
	}

	cout << isCorrectPart (ip);

	return 0;
}
'''
task1444c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n, m, w;
	cin >> n >> m >> w;

	int arr[34][34];
	for (int i (0); i <= n + 1; i++)
	{
		for (int j (0); j <= m + 1; j++)
		{
			arr[i][j] = 0;
		}
	}

	for (int i (0); i < w; i++)
	{
		int x, y;
		cin >> x >> y;

		arr[x][y] = -1000;
		arr[x - 1][y]++;
		arr[x - 1][y + 1]++;
		arr[x - 1][y - 1]++;
		arr[x + 1][y]++;
		arr[x + 1][y + 1]++;
		arr[x + 1][y - 1]++;
		arr[x][y + 1]++;
		arr[x][y - 1]++;
	}

	for (int i (1); i <= n; i++)
	{
		for (int j (1); j <= m; j++)
		{
			if (arr[i][j] < 0)
			{
				cout << "* ";
			} else
			{
				cout << arr[i][j] << ' ';
			}
		}
		cout << endl;
	}

	return 0;
}
'''
task1445c = '''
#include <iostream>

using namespace std;

int main ()
{
	int m, n, x, y;
	cin >> m >> n >> x >> y;

	if (x + 1 <= m)
	{
		cout << x + 1 << ' ' << y << endl;
	}
	if (y + 1 <= n)
	{
		cout << x << ' ' << y + 1 << endl;
	}
	if (x - 1 > 0)
	{
		cout << x - 1 << ' ' << y << endl;
	}
	if (y - 1 > 0)
	{
		cout << x << ' ' << y - 1;
	}

	return 0;
}
'''
task1448c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	cout << n << ' ';
	n %= 100;
	if (((n > 10) && (n < 20)) || (!(n % 10)) || (n % 10 >= 5))
	{
		cout << "bochek";
	} else
	{
		cout << ((n % 10 == 1) ? "bochka" : "bochki");
	}

	return 0;
}
'''
task1450c = '''
#include <iostream>
#include <string>

using namespace std;

bool isPalindrom (string s)
{
	for (int i (0); i <= s.length () / 2; i++)
	{
		if (s[i] != s[s.length () - 1 - i])
		{
			return false;
		}
	}

	return true;
}

int main ()
{
	string s;
	cin >> s;

	string result ("");
	for (int i (0); i < s.length (); i++)
	{
		string subS ("");
		for (int j (i); j < s.length (); j++)
		{
			subS += s[j];
			if (((subS.length () > result.length ())) && (isPalindrom (subS)))
			{
				result = subS;
			}
		}
	}

	cout << result;

	return 0;
}
'''
task1451c = '''
#include <iostream>
#include <cmath>

using namespace std;

int main ()
{
	int a, b, c;
	cin >> a >> b >> c;

	int s (abs (a % 2) + abs (b % 2) + abs (c % 2));

	cout << (((s) && (s != 3)) ? "YES" : "NO");

	return 0;
}
'''
task1456c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	int a[100];
	for (int i (0); i < n; i++)
	{
		cin >> a[i];
	}

	int h;
	cin >> h;
	
	for (int i (0); i < n; i++)
	{
		if (h > a[i])
		{
			cout << i + 1;
			return 0;
		}
	}
	
	cout << n + 1;

	return 0;
}
'''
task1457c = '''
#include <iostream>
#include <algorithm>

using namespace std;

int main ()
{
	int n, a, b, c, d;
	cin >> n >> a >> b >> c >> d;

	int arr[1000];
	for (int i (0); i < n; i++)
	{
		arr[i] = i + 1;
	}

	reverse (arr + a - 1, arr + b);
	reverse (arr + c - 1, arr + d);
	
	for (int i (0); i < n; i++)
	{
		cout << arr[i] << ' ';
	}

	return 0;
}
'''
task1458c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n, m;
	cin >> n >> m;

	int input[50][50], result[50][50];
	for (int i (0); i < n; i++)
	{
		for (int j (0); j < m; j++)
		{
			cin >> input[i][j];
		}
	}

	for (int i (0); i < n; i++)
	{
		for (int j (0); j < m; j++)
		{
			result[j][i] = input[n - i - 1][j];
		}
	}

	cout << m << ' ' << n << endl;
	for (int i (0); i < m; i++)
	{
		for (int j (0); j < n; j++)
		{
			cout << result[i][j] << ' ';
		}
		cout << endl;
	}

	return 0;
}
'''
task1459c = '''
#include <iostream>
using namespace std;
int main()
{
    int n;
    cin >> n;
    if(n == 100)
        cout << "C";
    else{
        switch(n / 10){
            case 1: cout << "X"; break;
            case 2: cout << "XX"; break;
            case 3: cout << "XXX"; break;
            case 4: cout << "XL"; break;
            case 5: cout << "L"; break;
            case 6: cout << "LX"; break;
            case 7: cout << "LXX"; break;
            case 8: cout << "LXXX"; break;
            case 9: cout << "XC"; break;
        }
        switch(n % 10){
            case 1: cout << "I"; break;
            case 2: cout << "II"; break;
            case 3: cout << "III"; break;
            case 4: cout << "IV"; break;
            case 5: cout << "V"; break;
            case 6: cout << "VI"; break;
            case 7: cout << "VII"; break;
            case 8: cout << "VIII"; break;
            case 9: cout << "IX"; break;
        }
    }
    return 0;
}
'''
task1460c = '''
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	vector<int> arr (n);
	for (int i (0); i < n; cin >> arr[i], i++);

	int k;
	cin >> k;
	k %= n;

	rotate (arr.begin (), ((k > 0) ? arr.end () : arr.begin ()) - k, arr.end ());

	for (int nn : arr)
	{
		cout << nn << ' ';
	}

	return 0;
}
'''
task1461c = '''
#include <iostream>
#include <vector>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	vector<int> arr (n);
	for (int i (0); i < n; i++)
	{
		cin >> arr[i];
	}

	int result (0);
	bool changed;
	do
	{
		changed = false;
		int prev (arr.back ()), count (1);

		for (int i (arr.size () - 2); i >= 0; i--)
		{
			if (arr[i] != prev)
			{
				count = 0;
				prev = arr[i];
			}

			count++;

			if (count == 3)
			{
				changed = true;
				arr.erase (arr.begin () + i, arr.begin () + i + 3);
				result += 3;
			} else if (count > 3)
			{
				arr.erase (arr.begin () + i, arr.begin () + i + 1);
				result++;
			}
		}
	} while (changed);

	cout << result;

	return 0;
}
'''
task1464c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	bool arr[50][50];
	for (int i (0); i < n; i++)
	{
		for (int j (0); j < n; j++)
		{
			arr[i][j] = (i == 0);
		}
	}

	for (int i (1), x (n - 1), y (0), dir (0), size (n + 1); i < n; i++, dir = ++dir % 4)
	{
		if (!(dir % 2))
		{
			size -= 2;
		}

		size += (i == n - 1);

		switch (dir)
		{
			case 0 :
				for (int j (0); j < size; j++)
				{
					arr[y++][x] = true;
				}
				break;

			case 1 :
				for (int j (0); j < size; j++)
				{
					arr[y][x--] = true;
				}
				break;

			case 2 :
				for (int j (0); j < size; j++)
				{
					arr[y--][x] = true;
				}
				break;

			case 3 :
				for (int j (0); j < size; j++)
				{
					arr[y][x++] = true;
				}
				break;
		}
	}

	for (int i (0); i < n; i++)
	{
		for (int j (0); j < n; j++)
		{
			cout << arr[i][j];
		}
		cout << endl;
	}

	return 0;
}
'''
task1466c = '''
#include <iostream>
#include <cmath>

using namespace std;

int main ()
{
	long long n;
	cin >> n;

	long long result (abs (n));
	if (result % 2)
	{
		result *= (1 + result) / 2;
	} else
	{
		result = result / 2 * (1 + result);
	}

	cout << ((n < 0) ? 1 - result : result);

	return 0;
}
'''
task1467c = '''
#include <iostream>

using namespace std;

int main ()
{
	int d, m, y;
	cin >> d >> m >> y;

	int month[] {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
	month[1] += ((!(y % 4) && (y % 100)) || (!(y % 400)));
	
	d += 2;
	if (d > month[m - 1])
	{
		d -= month[m - 1];
		m++;
	}

	if (m > 12)
	{
		m = 1;
		y++;
	}

	cout << d << ' ' << m << ' ' << y;

	return 0;
}
'''
task1468c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	int month[] {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
	
	int y (n % 10000), m (n / 10000 % 100), d (n / 1000000 % 100);

	month[1] += ((!(y % 4) && (y % 100)) || (!(y % 400)));

	int result (d);
	for (int i (1); i < y; result += (((!(i % 4) && (i % 100)) || (!(i % 400))) ? 366 : 365), i++);
	for (int i (0); i < m - 1; i++)
	{
		result += month[i];
	}

	cout << result;

	return 0;
}
'''
task1475c = ''' 
#include <iostream>

using namespace std;

int main ()
{
	int k;
	cin >> k;

	cout << "It is " << k / 3600 << " hours " << k % 3600 / 60 << " minutes.";

	return 0;
}
'''
task1476c = '''
#include <iostream>

using namespace std;

int main ()
{
	int k;
	cin >> k;

	cout << "It is " << k / 30 << " hours " << k % 30 * 2 << " minutes.";

	return 0;
}
'''
task1479c = '''
#include <iostream>

using namespace std;

int main ()
{
	int k, n;
	cin >> k >> n;

	cout << (n - 1) / k + 1 << ' ' << (n - 1) % k + 1;

	return 0;
}
'''
task1483c = '''
#include <iostream>

using namespace std;

int main ()
{
	int h1, m1, s1, h2, m2, s2;
	cin >> h1 >> m1 >> s1 >> h2 >> m2 >> s2;

	cout << 3600 * h2 + 60 * m2 + s2 - 3600 * h1 - 60 * m1 - s1;

	return 0;
}
'''
task201c= '''

#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	int f1 (1), f2 (1);
	for (int i (0), tmp; i < n - 1; i++)
	{
		tmp = f1 + f2;
		f1 = f2;
		f2 = tmp;
	}

	cout << f1;

	return 0;
}
'''
task203c = '''

#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	int a[3]{1, 2, 4};
	for (int i (0), tmp; i < n - 1; i++)
	{
		tmp = a[0] + a[1] + a[2];
		a[0] = a[1];
		a[1] = a[2];
		a[2] = tmp;
	}

	cout << a[0];

	return 0;
}
'''
task208c = '''

#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	for (int i (0); i < n; i++)
	{
		int a;
		cin >> a;

		if (!(i % 2))
		{
			cout << a << ' ';
		}
	}

	return 0;
}
'''
task234c = '''
#include <iostream>
#include <algorithm>

using namespace std;

int main ()
{
    int n, m;
    cin >> n >> m;

    if (m == 1605)
    {
        cout << 1;
        return 0;
    }

    int nn (max (n, 1605) - 1605), mm (max (m, 1605) - 1605);
    int result ((mm - nn + nn % 10) / 10);
    cout << result + ((n < 1605) && (m >= 1605));

    return 0;
}
'''
task236c = '''
#include <iostream>
#include <cmath>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	int lsp (sqrt (n));
	int ls (lsp * lsp), rs (pow (lsp + 1, 2));

	if ((n != ls + 1) && (n != ls))
	{
		cout << ls - (rs - n) + 1 << ' ';
	}

	if ((n != ls + 1) && (n != 1))
	{
		cout << n - 1 << ' ';
	}

	if (n != ls)
	{
		cout << n + 1 << ' ';
	}

	cout << n + 2 * (lsp + (n != ls));


	return 0;
}
'''
task238c = '''
#include <iostream>
#include <cmath>

using namespace std;

int main ()
{
    int n;
    cin >> n;

    int p1 (0), p2 (0);
    for (int i (0); i < n; i++)
    {
        int v1, t1, v2, t2;
        cin >> v1 >> t1 >> v2 >> t2;

        p1 = (p1 + 400 + (v1 * t1) % 400) % 400;
        p2 = (p2 + 400 + (v2 * t2) % 400) % 400;
    }

    cout << abs (p1 - p2);

    return 0;
}
'''
task243c = '''
#include <iostream>

using namespace std;

int main ()
{
    int p, n, s (0);
    cin >> p >> n;

    for (int i (0), a; i < n; i++)
    {
        cin >> a;
        s += a;
    }

    for (int i (0); i < s - p; i++)
    {
        cout << 1 << ' ';
    }

    return 0;
}
'''
task247c = '''
#include <iostream>

using namespace std;

int main ()
{
    int n;
    cin >> n;

    for (int i (0); n - i >= 0; i += 5)
    {
        if (!((n - i) % 3))
        {
            cout << (n - i) / 3 << ' ' << i / 5;
            return 0;
        }
    }

    cout << "IMPOSSIBLE";

    return 0;
}
'''
task252c = '''
#include <iostream>

using namespace std;

double power (double a, int n)
{
    if (n < 0)
    {
        return 1 / power (a, -n);
    }

    return ((n) ? a * power (a, n - 1) : 1);
}

int main ()
{
    double a;
    int n;
    cin >> a >> n;

    cout << power (a, n);

    return 0;
}
'''
task253c = '''
#include <iostream>

using namespace std;

int main ()
{
    int n;
    cin >> n;

    cout << ((((n % 4 == 0) && (n % 100 != 0)) || (n % 400 == 0)) ? "YES" : "NO");

    return 0;
}
'''
task254c = '''
#include <iostream>

using namespace std;

int main ()
{
    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;

    cout << (((x1 == x2) || (y1 == y2)) ? "YES" : "NO");

    return 0;
}
'''
task255c = '''
#include <iostream>
#include <cmath>

using namespace std;

int main ()
{
    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;

    cout << ((abs (x1 - x2) == abs (y1 - y2)) ? "YES" : "NO");

    return 0;
}
'''
task256c = '''
#include <iostream>
#include <cmath>

using namespace std;

int main ()
{
    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;

    cout << (((abs (x1 - x2) == abs (y1 - y2)) || (x1 == x2) || (y1 == y2)) ? "YES" : "NO");

    return 0;
}
'''
task257c = '''
#include <iostream>
#include <cmath>

using namespace std;

int main ()
{
    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;

    int dx (abs (x1 - x2));
    int dy (abs (y1 - y2));

    cout << ((((dx == 1) && (dy == 2)) || ((dx == 2) && (dy == 1))) ? "YES" : "NO");

    return 0;
}
'''
task258c = '''
#include <iostream>

using namespace std;

int main ()
{
    int n, m, k;
    cin >> n >> m >> k;

    cout << ((((k % n == 0) || (k % m == 0)) && (n * m >= k)) ? "YES" : "NO");

    return 0;
}
'''
task259c = '''
#include <iostream>

using namespace std;

int main ()
{
    int k;
    cin >> k;

    cout << (((k % 4 == 0) || (k == 1)) ? "YES" : "NO");

    return 0;
}
'''
task260c = '''
#include <iostream>

using namespace std;

int main ()
{
    int a, b;
    cin >> a >> b;

    if ((!a) && (!b))
    {
        cout << "INF";
    }
    else if ((!a) || (b % a))
    {
        cout << "NO";
    } else
    {
        cout << -b / a;
    }

    return 0;
}
'''
task261c = '''
#include <iostream>

using namespace std;

int main ()
{
    int a, b, c, d, x;
    cin >> a >> b >> c >> d;

    if ((!a) && (!b))
    {
        cout << "INF";
    } else if ((a) && (!(b % a)) && ((x = -b / a) * c + d))
    {
        cout << x;
    } else
    {
        cout << "NO";
    }

    return 0;
}
'''
task262c = '''
#include <iostream>

using namespace std;

int main ()
{
	int a, b, c, d;
	cin >> a >> b >> c >> d;

	int n (c * 100 + d - a * 100 - b);

	cout << n / 100 << ' ' << n % 100;

	return 0;
}
'''
task264c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	cout << (((n == 1) || (n == 2) || (n == 4) || (n == 7) ? "NO" : "YES"));

	return 0;
}
'''
task265c = '''
#include <iostream>

using namespace std;

int main ()
{
	int k, m, n;
	cin >> k >> m >> n;

	if (n <= k)
	{
		cout << m * 2;
	} else
	{
		int count (2 * n);
		cout << (count / k + (count % k != 0)) * m;
	}

	return 0;
}
'''
task266c = '''
#include <iostream>

using namespace std;

int main ()
{
	int x1, y1, x2, y2;
	cin >> x1 >> y1 >> x2 >> y2;

	cout << (((x1 * x2 > 0) && (y1 * y2 > 0)) ? "YES" : "NO");

	return 0;
}
'''
task279c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	pair<int, int> farPoint (0, 0);
	int farDistance (0);

	for (int i (0); i < n; i++)
	{
		int x, y;
		cin >> x >> y;

		int distance (x * x + y * y);
		if (distance > farDistance)
		{
			farPoint = make_pair (x, y);
			farDistance = distance;
		}
	}

	cout << farPoint.first << ' ' << farPoint.second;

	return 0;
}
'''
task2796c = '''
#include <iostream>
#include <string>

using namespace std;

int main ()
{
	string x;
	int n;
	cin >> x >> n;

	for (int i (1); i < n; i++)
	{
		string it ("");

		char prevChar (x[0]);
		int count (1);
		for (int j (1); j < x.length (); j++)
		{
			if (x[j] != prevChar)
			{
				it += to_string (count) + prevChar;

				prevChar = x[j];
				count = 0;
			}

			count++;
		}

		x = it + to_string (count) + prevChar;
	}

	cout << x;

	return 0;
}
'''
task2797c = '''
#include <iostream>

using namespace std;

int main ()
{
	int result (0);
	char c;
	while (cin >> c)
	{
		if ((c == '6') || (c == '9') || (c == '0'))
		{
			result++;
		} else if (c == '8')
		{
			result += 2;
		}
	}

	cout << result;

	return 0;
}
'''
task282c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	int arr[100][100];
	for (int i (0); i < n; i++)
	{
		for (int j (0); j < n; j++)
		{
			arr[i][j] = (n - i - 1 == j) + 2 * (n - i - 1 < j);
		}
	}

	for (int i (0); i < n; i++)
	{
		for (int j (0); j < n; j++)
		{
			cout << arr[i][j] << ' ';
		}
		cout << endl;
	}

	return 0;
}
'''
task292c = '''
#include <iostream>

using namespace std;

int main ()
{
    int n, m;
    cin >> n >> m;

    cout << ((n > m) ? n : m);

    return 0;
}
'''
task293c = '''
#include <iostream>

using namespace std;

int main ()
{
    int a, b;
    cin >> a >> b;

    if (a == b)
    {
        cout << 0;
    } else
    {
        cout << (a > b ? 1 : 2);
    }

    return 0;
}
'''
task2936c = '''
#include <iostream>
#include <cmath>

using namespace std;

int main ()
{
	int a, b;
	cin >> a >> b;
	cout << sqrt (a * a + b * b);

	return 0;
}
'''
task2937c = '''
#include <iostream>

using namespace std;

int main ()
{
	int b;
	cin >> b;

	cout << "The next number for the number " << b << " is " << b + 1 << "." << endl;
	cout << "The previous number for the number " << b << " is " << b - 1 << ".";

	return 0;
}
'''
task2938c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n, k;
	cin >> n >> k;

	cout << k / n;

	return 0;
}
'''
task2939c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n, k;
	cin >> n >> k;

	cout << k % n;

	return 0;
}
'''
task294c = '''
#include <iostream>
#include <algorithm>

using namespace std;

int main ()
{
    int a, b, c;
    cin >> a >> b >> c;

    cout << max (max (a, b), c);

    return 0;
}
'''
task2940c = '''
#include <iostream>

using namespace std;

int main ()
{
	int v, t;
	cin >> v >> t;

	cout << ((v * t) % 109 + 109) % 109;

	return 0;
}
'''
task2941c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	cout << n % 10;

	return 0;
}
'''
task2942c = '''
#include <iostream>

using namespace std;

int main ()
{
    int n;
    cin >> n;

    cout << n / 10;

    return 0;
}
'''
task2943c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	cout << n / 10 % 10;

	return 0;
}
'''
task2944c = '''
#include <iostream>

using namespace std;

int main ()
{
    int n;
    cin >> n;

    cout << n % 10 + n / 10 % 10 + n / 100;

    return 0;
}
'''
task2945c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	cout << n + 2 - (n % 2);

	return 0;
}
'''
task2947c = '''
#include <iostream>

using namespace std;

int main ()
{
    int n;
    cin >> n;

    n %= 24 * 60;

    cout << n / 60 << ' ' << n % 60;

    return 0;
}
'''
task2948c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	int h ((n / 3600) % 24);
	n %= 3600;

	int m (n / 60);
	n %= 60;

	cout << h << ':' << m / 10 % 10 << m % 10 << ':' << n / 10 % 10 << n % 10;

	return 0;
}
'''
task2949c = '''
#include <iostream>

using namespace std;

int main ()
{
    int a, b;
    cin >> a >> b;

	int c (b);
	b = a;
	a = c;

    cout << a << ' ' << b;

    return 0;
}
'''
task295c = '''
#include <iostream>
#include <algorithm>

using namespace std;

int main ()
{
	int a[3];
	cin >> a[0] >> a[1] >> a[2];

	sort (a, a + 3);

	cout << ((a[0] + a[1] > a[2]) ? "YES" : "NO");

	return 0;
}
'''
task2950c = '''
#include <iostream>
#include <cmath>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	int m (9 * 60 + n * 45 + ((n - 1) / 2) * 15 + round ((n - 1) / 2.) * 5);
	cout << m / 60 << ' ' << m % 60;

	return 0;
}
'''
task2951c = '''
#include <iostream>

using namespace std;

int main ()
{
    int a, b, n;
    cin >> a >> b >> n;

    a = (a * 100 + b) * n;

    cout << a / 100 << ' ' << a % 100;

    return 0;
}
'''
task2952c = '''
#include <iostream>

using namespace std;

int main ()
{
	int h1, m1, s1, h2, m2, s2;
	cin >> h1 >> m1 >> s1 >> h2 >> m2 >> s2;

	cout << h2 * 3600 + m2 * 60 + s2 - (h1 * 3600 + m1 * 60 + s1);

	return 0;
}
'''
task2953c = '''
#include <iostream>
#include <cmath>

using namespace std;

int main ()
{
    int n, m;
    cin >> n >> m;

    cout << ceilf (m / (n + 0.));

    return 0;
}
'''
task2954c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n, k;
	cin >> n >> k;

	cout << (n - (k % n)) % n;

	return 0;
}
'''
task2956c = '''
#include <iostream>
#include <cmath>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	cout << abs (n % 10 - n / 1000) + abs (n / 10 % 10 - n / 100 % 10) + 1;

	return 0;
}
'''
task2957c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n, m;
	cin >> n >> m;

	cout << n % m * (m % n) + 1;

	return 0;
}
'''
task2959c = '''
#include <iostream>

using namespace std;

int main ()
{
    int n;
    cin >> n;

    if (!n)
    {
        cout << 0;
    } else
    {
        cout << (n > 0 ? 1 : -1);
    }

    return 0;
}
'''
task296c = '''

#include <iostream>

using namespace std;

int main ()
{
	int a, b, c;
	cin >> a >> b >> c;

	if ((a == b) && (b == c))
	{
		cout << 3;
	} else
	{
		cout << (((a == b) || (b == c) || (a == c)) ? 2 : 0);
	}

	return 0;
}
'''
task2960c = '''
#include <iostream>

using namespace std;

int main ()
{
    int a, b;
    cin >> a >> b;

    cout << ((((a == 1) && (b == 1)) || ((a != 1) && (b != 1))) ? "YES" : "NO");

    return 0;
}
'''
task2961c = '''
#include <iostream>
#include <algorithm>

using namespace std;

int main ()
{
	int a[3];
	cin >> a[0] >> a[1] >> a[2];

	sort (a, a + 3);

	cout << a[0] << ' ' << a[1] << ' ' << a[2];

	return 0;
}
'''
task298c = '''
#include <iostream>
#include <cmath>

using namespace std;

int main ()
{
    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;

    cout << (((abs (x1 - x2) <= 1) && (abs (y1 - y2) <= 1)) ? "YES" : "NO");

    return 0;
}
'''
task300c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	const int month[] {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
	
	int m (0);
	for (; ((m < 12) && (month[m] < n)); n -= month[m], m++);

	cout << n << ' ' << m + 1;

	return 0;
}
'''
task301c = '''
#include <iostream>
#include <cmath>

using namespace std;

int main ()
{
	float a, b, c;
	cin >> a >> b >> c;

	float d (b * b - 4 * a * c);
	if (d > 0)
	{
		a *= 2;
		cout << (-b - sqrt (d)) / a << ' ' << (-b + sqrt (d)) / a;
	} else if (!d)
	{
		cout << -b / (2 * a);
	}

	return 0;
}
'''
task302c = '''
#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

int main ()
{
	int a[3];
	cin >> a[0] >> a[1] >> a[2];

	sort (a, a + 3);

	if (a[0] + a[1] <= a[2])
	{
		cout << "impossible";
		return 0;
	}

	a[0] = pow (a[0], 2) + pow (a[1], 2);
	a[2] = pow (a[2], 2);

	if (a[0] == a[2])
	{
		cout << "right";
	} else
	{
		cout << ((a[0] > a[2]) ? "acute" : "obtuse");
	}

	return 0;
}
'''
task3024c = '''
#include <iostream>
#include <cmath>

using namespace std;

float length (int x1, int y1, int x2, int y2)
{
    return sqrt (pow (x1 - x2, 2) + pow (y1 - y2, 2));
}

int main ()
{
    int x1, y1, x2, y2, x3, y3;
    cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;

    cout << fixed << length (x1, y1, x2, y2) + length (x1, y1, x3, y3) + length (x2, y2, x3, y3);

    return 0;
}
'''
task303c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	cout << n << ' ';
	if (((n > 10) && (n < 20)) || (!(n % 10)) || (n % 10 >= 5))
	{
		cout << "korov";
	} else
	{
		cout << ((n % 10 == 1) ? "korova" : "korovy");
	}

	return 0;
}
'''
task304c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	int a (n / 60);
	n %= 60;
	if (n > 34)
	{
		n = 0;
		a++;
	}

	int b (n / 10);
	n %= 10;
	if (n == 9)
	{
		n = 0;
		b++;
	}
	
	cout << n << ' ' << b << ' ' << a;

	return 0;
}
'''
task305c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	int a (n / 60);
	n %= 60;
	if (n > 35)
	{
		n = 0;
		a++;
	}

	int b (n / 20);
	n %= 20;
	if (n > 17)
	{
		n = 0;
		b++;
	}

	int c (n / 10);
	n %= 10;
	if (n == 9)
	{
		n = 0;
		c++;
	}
	
	cout << n % 5 << ' ' << n / 5 <<  ' ' << c << ' ' << b << ' ' << a;

	return 0;
}
'''
task3058c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	int i (2);
	while (n % i)
	{
		i++;
	}

	cout << i;

	return 0;
}
'''
task3059c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	int i (1);
	while (i <= n)
	{
		cout << i << ' ';
		i *= 2;
	}

	return 0;
}
'''
task306c = '''
#include <iostream>

using namespace std;

int min (int a, int b, int c, int d)
{
	int e ((a < b) ? a : b), f ((c < d) ? c : d);

	return ((e < f) ? e : f);
}

int main ()
{
	int a, b, c, d;
	cin >> a >> b >> c >> d;

	cout << min (a, b, c, d);

	return 0;
}
'''
task3060c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	while (!(n % 2))
	{
		n /= 2;
	}

	cout << ((n == 1) ? "YES" : "NO");

	return 0;
}
'''
task3061c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	int result (0), a (1);
	while (a < n)
	{
		a *= 2;
		result++;
	}

	cout << result;

	return 0;
}
'''
task3062c = '''
#include <iostream>

using namespace std;

int main ()
{
	float x, y;
	cin >> x >> y;

	int result (1);
	while (x < y)
	{
		x *= 1.1;
		result++;
	}

	cout << result;

	return 0;
}
'''
task3063c = '''
#include <iostream>

using namespace std;

int main ()
{
	float x, y;
	cin >> x >> y;

	int result (1);
	while (x < y)
	{
		x *= 1.1;
		result++;
	}

	cout << result;

	return 0;
}
'''
task3064c = '''
#include <iostream>

using namespace std;

int main ()
{
	int a, result (-1);
	do
	{
		cin >> a;
		result++;
	} while (a);

	cout << result;

	return 0;
}
'''
task3065c = '''
#include <iostream>

using namespace std;

int main ()
{
	int a, result (0);
	do
	{
		cin >> a;
		result += a;
	} while (a);

	cout << result;

	return 0;
}
'''
task3066c = '''
#include <iostream>

using namespace std;

int main ()
{
	int a, sum (0), n (-1);
	do
	{
		cin >> a;
		sum += a;
		n++;
	} while (a);

	cout << (float) sum / n;

	return 0;
}
'''
task3067c = '''
#include <iostream>

using namespace std;

int main ()
{
	int a, result (-1);
	do
	{
		cin >> a;
		result += !(a % 2);
	} while (a);

	cout << result;

	return 0;
}
'''
task3068c = '''
#include <iostream>
#include <algorithm>

using namespace std;

int main ()
{
	int a, result (0);
	do
	{
		cin >> a;
		result = max (a, result);
	} while (a);

	cout << result;

	return 0;
}
'''
task3069c = '''
#include <iostream>

using namespace std;

int main ()
{
	int a, b, result (0);
	cin >> b;
	do
	{
		cin >> a;
		result += a > b;
		swap (a, b);
	} while (b);

	cout << result;

	return 0;
}
'''
task307c = '''
#include <iostream>

using namespace std;

double power (double a, int n)
{
	return ((n) ? a * power (a, n - 1) : 1);
}

int main ()
{
	double a;
	int n;
	cin >> a >> n;

	cout << power (a, n);

	return 0;
}
'''
task3070c = '''
#include <iostream>

using namespace std;

int main ()
{
	int a, m1 (0), m2 (0);
	do
	{
		cin >> a;
		if (a > m1)
		{
			m2 = m1;
			m1 = a;
		} else if (a > m2)
		{
			m2 = a;
		}
	} while (a);

	cout << m2;

	return 0;
}
'''
task3071c = '''
#include <iostream>

using namespace std;

int main ()
{
	int a, m1 (0), m2 (0);
	do
	{
		cin >> a;
		if (a > m1)
		{
			m2 = m1;
			m1 = a;
		} else if (a > m2)
		{
			m2 = a;
		}
	} while (a);

	cout << m2;

	return 0;
}
'''
task3072c = '''
#include <iostream>

using namespace std;

int main ()
{
	int a, m (0), result (0);
	do
	{
		cin >> a;
		if (a > m)
		{
			m = a;
			result = 1;
		} else if (a == m)
		{
			result++;
		}
	} while (a);

	cout << result;

	return 0;
}
'''
task3073c = '''
#include <iostream>

using namespace std;

int main ()
{
	int a (1), sum (0);
	bool prev0 (false);

	while ((a) || (!prev0))
	{
		prev0 = !a;
		cin >> a;
		sum += a;
	}

	cout << sum;

	return 0;
}
'''
task3074c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	int f1 (0), f2 (1), i (0);
	while (i < n)
	{
		int tmp (f1 + f2);
		f1 = f2;
		f2 = tmp;
		i++;
	}

	cout << f1;

	return 0;
}
'''
task3075c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	int f1 (0), f2 (1), i (0);
	while (f1 < n)
	{
		int tmp (f1 + f2);
		f1 = f2;
		f2 = tmp;
		i++;
	}

	cout << ((f1 == n) ? i : -1);

	return 0;
}
'''
task3076c = '''
#include <iostream>

using namespace std;

int main ()
{
	int a, b;
	cin >> a >> b;

	while (a != b)
	{
		if ((!(a % 2)) && (a / 2 >= b))
		{
			a /= 2;
			cout << ":2" << endl;
		} else
		{
			a--;
			cout << -1 << endl;
		}
	}

	return 0;
}
'''
task3077c = '''
#include <iostream>
#include <algorithm>

using namespace std;

int main ()
{
	int a, b, curEquals (1), maxEquals (0);
	cin >> a;
	do
	{
		cin >> b;
		if (b == a)
		{
			curEquals++;
		} else
		{
			maxEquals = max (maxEquals, curEquals);
			curEquals = 1;
		}
		a = b;
	} while (a);

	cout << maxEquals;

	return 0;
}
'''
task3078c = '''
#include <iostream>
#include <algorithm>

using namespace std;

int main ()
{
	int a, b, curMonotonous (1), maxMonotonous (0);
	bool mode (false);
	cin >> a;
	while (true)
	{
		cin >> b;

		if (!b)
		{
			break;
		}

		if (((a > b) && (mode)) || ((a < b) && (!mode)))
		{
			curMonotonous++;
		} else
		{
			maxMonotonous = max (maxMonotonous, curMonotonous);
			curMonotonous = 2;
			if (a > b)
			{
				mode = true;
			} else if (a < b)
			{
				mode = false;
			} else
			{
				curMonotonous = 1;
			}
		}
		a = b;
	}

	cout << max (maxMonotonous, curMonotonous);

	return 0;
}
'''
task3079c = '''
#include <iostream>

using namespace std;

int main ()
{
	int a, b, c, result (0);
	cin >> a >> b;
	while (true)
	{
		cin >> c;

		if (!c)
		{
			break;
		}

		if ((b > a) && (b > c))
		{
			result++;
		}

		a = b;
		b = c;
	}

	cout << result;

	return 0;
}
'''
task308c = '''
#include <iostream>

using namespace std;

bool Xor (bool x, bool y)
{
	return (x + y == 1);
}

int main ()
{
	bool x, y;
	cin >> x >> y;

	cout << Xor (x, y);

	return 0;
}
'''
task3080c = '''
#include <iostream>
#include <algorithm>

using namespace std;

int main ()
{
	int a, b, c, prevPos (-1), minDistance (-1), i (0);
	cin >> a >> b;
	while (true)
	{
		cin >> c;

		if (!c)
		{
			break;
		}

		if ((b > a) && (b > c))
		{
			if (prevPos == -1)
			{
				prevPos = i;
			} else
			{
				int distance (i - prevPos);
				prevPos = i;
				minDistance = (minDistance == -1) ? distance : min (minDistance, distance);
			}
		}

		a = b;
		b = c;
		i++;
	}

	cout << ((minDistance == -1) ? 0 : minDistance);

	return 0;
}
'''
task3081c = '''
#include <iostream>
#include <cmath>

using namespace std;

int main ()
{
	int a, sum (0), sum2 (0), n (-1);
	do
	{
		cin >> a;
		
		sum += a;
		sum2 += a * a;
		n++;
	} while (a);

	float s (sum / (float) n);

	cout << sqrt ((sum2 - 2 * sum * s + s * s * n) / (n - 1));

	return 0;
}
'''
task3082c = '''
#include <iostream>
#include <sstream>

using namespace std;

struct Jug
{
	int lim;
	char name;
};

int main ()
{
	int n;
	Jug a {-1, 'A'}, b {-1, 'B'};
	cin >> a.lim >> b.lim >> n;

	if (a.lim > b.lim)
	{
		swap (a, b);
	}

	if (n == b.lim)
	{
		cout << ">" << b.name;
		return 0;
	}

	int ss (0);
	stringstream result;
	do
	{
		ss += a.lim;

		result << ">" << a.name << endl;
		result << a.name << ">" << b.name << endl;

		if (ss >= b.lim)
		{
			result << b.name << ">" << endl << a.name << ">" << b.name << endl;
			ss %= b.lim;
		}

		if (ss == n)
		{
			cout << result.str ();
			return 0;
		}
	} while (ss);

	cout << "Impossible";

	return 0;
}
'''
task309c = '''
#include <iostream>

using namespace std;

bool Election (bool x, bool y, bool z)
{
	return (x + y + z >= 2);
}

int main ()
{
	bool x, y, z;
	cin >> x >> y >> z;

	cout << Election (x, y, z);

	return 0;
}
'''
task310c = '''
#include <iostream>
#include <cmath>

using namespace std;

int main ()
{
    int n;
    cin >> n;

    for (int i = 2; i <= sqrt (n); i++)
    {
        if (n % i == 0)
        {
            cout << "composite";
            return 0;
        }
    }

    cout << "prime";

    return 0;
}
'''
task311c = '''
#include <iostream>

using namespace std;

double power (double a, int n)
{
    if (!n)
    {
        return 1;
    }

    if (n % 2)
    {
        return a * power (a, n - 1);
    }

    return power (a * a, n / 2);
}

int main ()
{
    double a;
    int n;

    cin >> a >> n;
    cout << power (a, n);

    return 0;
}
'''
task3116c = '''
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main ()
{
	string s;
	getline (cin, s);	

	cout << s[2] << endl;
	cout << s[s.length () - 2] << endl;
	cout << s.substr (0, 5) << endl;
	cout << s.substr (0, s.length () - 2) << endl;
	for (int i (0); i < s.length (); i += 2)
	{
		cout << s[i];
	}
	cout << endl;
	for (int i (1); i < s.length (); i += 2)
	{
		cout << s[i];
	}
	cout << endl;
	reverse (s.begin (), s.end ());
	cout << s << endl;
	for (int i (0); i < s.length (); i += 2)
	{
		cout << s[i];
	}
	cout << endl;
	cout << s.length ();

	return 0;
}
'''
task3117c = '''
#include <iostream>
#include <string>

using namespace std;

int main ()
{
	string s;
	int count (0);
	for (; cin >> s; count++);

	cout << count;

	return 0;
}
'''
task3118c = '''
#include <iostream>
#include <string>

using namespace std;

int main ()
{
	string s;
	cin >> s;

	int hlen (s.length () / 2 + s.length () % 2);
	cout << s.substr (hlen) << s.substr (0, hlen) << endl;

	return 0;
}
'''
task3119c = '''
#include <iostream>
#include <string>

using namespace std;

int main ()
{
	string a, b;
	cin >> a >> b;

	cout << b << ' ' << a << endl;

	return 0;
}
'''
task312c = '''
#include <iostream>

using namespace std;

int phi (int n)
{
	int a (1), b (1);
	for (int i = 0; i < n - 1; i++)
	{
		int tmp (a);
		a = b;
		b += tmp;
	}

	return b;
}

int main ()
{
	int n;
	cin >> n;

	cout << phi (n);

	return 0;
}
'''
task3120c = '''
#include <iostream>
#include <string>

using namespace std;

int main ()
{
	string s;
	getline (cin, s);

	int fpos (s.find ('f'));
	int lpos (s.rfind ('f'));
	if (fpos != string::npos)
	{
		cout << fpos;
		if (fpos != lpos)
		{
			cout << ' ' << lpos;
		}
	}

	return 0;
}
'''
task3121c = '''
#include <iostream>
#include <string>

using namespace std;

int main ()
{
	string s;
	getline (cin, s);

	int fpos (s.find ('f'));
	int spos (s.find ('f', fpos + 1));
	if (fpos == string::npos)
	{
		cout << -2;
	} else
	{
		cout << (spos == string::npos ? -1 : spos);
	}

	return 0;
}
'''
task3122c = '''
#include <iostream>
#include <string>

using namespace std;

int main ()
{
	string s;
	getline (cin, s);

	int pos (s.find('h'));
	s.erase (pos, s.rfind ('h') - pos + 1);

	cout << s << endl;

	return 0;
}
'''
task3123c = '''
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main ()
{
	string s;
	getline (cin, s);

	reverse (s.begin () + s.find ('h') + 1, s.begin () + s.rfind ('h'));

	cout << s << endl;

	return 0;
}
'''
task3124c = '''
#include <iostream>
#include <string>

using namespace std;

int main ()
{
	string s;
	getline (cin, s);

	int pos (s.find ('h') + 1);
	s.insert (pos, s.substr (pos, s.rfind ('h') - pos));

	cout << s << endl;

	return 0;
}
'''
task3125c = '''
#include <iostream>
#include <string>

using namespace std;

int main ()
{
	string s;
	getline (cin, s);

	for (char c : s)
	{
		if (c == '1')
		{
			cout << "one";
		} else
		{
			cout << c;
		}
	}
	cout << endl;

	return 0;
}
'''
task3126c = '''
#include <iostream>
#include <string>

using namespace std;

int main ()
{
	string s;
	getline (cin, s);

	for (char c : s)
	{
		if (c != '@')
		{
			cout << c;
		}
	}
	cout << endl;

	return 0;
}
'''
task3127c = '''
#include <iostream>
#include <string>

using namespace std;

int main ()
{
	string s;
	getline (cin, s);

	int lpos (s.find ('h'));
	int rpos (s.rfind ('h'));
	for (int i (0); i < s.length (); i++)
	{
		cout << (((s[i] == 'h') && (i > lpos) && (i < rpos)) ? 'H' : s[i]);
	}
	cout << endl;

	return 0;
}
'''
task3128c = '''
#include <iostream>
#include <string>

using namespace std;

int main ()
{
	string s;
	getline (cin, s);

	cout << s[0];
	for (int i (1); i < s.length (); i++)
	{
		cout << '*' << s[i];
	}
	cout << endl;

	return 0;
}
'''
task3129c = '''
#include <iostream>
#include <string>

using namespace std;

int main ()
{
	string s;
	getline (cin, s);

	for (int i (0); i < s.length (); i++)
	{
		if (i % 3)
		{
			cout << s[i];
		}
	}
	cout << endl;

	return 0;
}
'''
task313c = '''
#include <iostream>

using namespace std;

int c (int n, int k)
{
	if ((n == k) || (!k))
	{
		return 1;
	}
	return c (n - 1, k - 1) + c (n - 1, k);
}

int main ()
{
	int n, k;
	cin >> n >> k;

	cout << c (n, k);

	return 0;
}
'''
task315c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	int result (1);
	for (int i (2); i <= n; i++)
	{
		result += i * i;
	}

	cout << result;

	return 0;
}
'''
task3152c = '''
#include <iostream>

using namespace std;

int main ()
{
	for (int i (0), a; cin >> a; i++)
	{
		if (!(i % 2))
		{
			cout << a << ' ';
		}
	}

	return 0;
}
'''
task3153c = '''
#include <iostream>

using namespace std;

int main ()
{
	for (int a; cin >> a;)
	{
		if (!(a % 2))
		{
			cout << a << ' ';
		}
	}

	return 0;
}
'''
task3154c = '''
#include <iostream>

using namespace std;

int main ()
{
	int result (0);
	for (int a; cin >> a;)
	{
		if (a > 0)
		{
			result++;
		}
	}

	cout << result;

	return 0;
}
'''
task3155c = '''
#include <iostream>

using namespace std;

int main ()
{
	int a;
	cin >> a;

	for (int b; cin >> b;)
	{
		if (b > a)
		{
			cout << b << ' ';
		}

		a = b;
	}

	return 0;
}
'''
task3156c = '''
#include <iostream>

using namespace std;

int main ()
{
	int prev;
	cin >> prev;

	for (int a; cin >> a;)
	{
		if (a * prev > 0)
		{
			cout << prev << ' ' << a;
			return 0;
		}
		prev = a;
	}

	return 0;
}
'''
task3157c = '''
#include <iostream>
#include <climits>

using namespace std;

int main ()
{
	int result (0);
	for (int a (INT_MAX), b (INT_MAX), c; cin >> c;)
	{
		if ((b > a) && (b > c))
		{
			result++;
		}
		a = b;
		b = c;
	}

	cout << result;

	return 0;
}
'''
task3158c = '''
#include <iostream>

using namespace std;

int main ()
{
	int result, ind (0);
	cin >> result;

	for (int i (1), a; cin >> a; i++)
	{
		if (a > result)
		{
			result = a;
			ind = i;
		}
	}
	
	cout << result << ' ' << ind;

	return 0;
}
'''
task3159c = '''
#include <iostream>
#include <climits>

using namespace std;

int main ()
{
	int min (INT_MAX);
	for (int a; cin >> a;)
	{
		if ((a > 0) && (a < min))
		{
			min = a;
		}
	}

	cout << min;

	return 0;
}
'''
task316c = '''
#include <iostream>

using namespace std;

int main ()
{
    int n;
    cin >> n;

    int count (1);
    for (int i (2); i <= n; count *= i, i++);

    cout << count;

    return 0;
}
'''
task3160c = '''
#include <iostream>
#include <climits>

using namespace std;

int main ()
{
	long long min (LLONG_MAX);
	for (int a; cin >> a;)
	{
		if ((a % 2) && (a < min))
		{
			min = a;
		}
	}

	cout << ((min != LLONG_MAX) ? min : 0);

	return 0;
}
'''
task3161c = '''
#include <iostream>
#include <sstream>
#include <string>

using namespace std;

int main ()
{
	string line;
	getline (cin, line);

	int x;
	cin >> x;

	stringstream ss (line);
	int i (0);
	for (int a; ss >> a; i++)
	{
		if (x > a)
		{
			cout << i + 1;
			return 0;
		}
	}

	cout << i + 1;

	return 0;
}
'''
task3162c = '''
#include <iostream>

using namespace std;

int main ()
{
	int prev, result (1);
	cin >> prev;

	for (int a; cin >> a;)
	{
		result += (prev != a);
		prev = a;
	}
	
	cout << result;

	return 0;
}
'''
task3163c = '''
#include <iostream>
#include <vector>

using namespace std;

int main ()
{
	vector<int> n;
	int a;

	while (cin >> a)
	{
		n.push_back (a);
	}

	for (int i (n.size () - 1); i >= 0; i--)
	{
		cout << n[i] << ' ';
	}

	return 0;
}
'''
task3164c = '''
#include <iostream>
#include <vector>

using namespace std;

int main ()
{
	vector<int> n;
	int a;

	while (cin >> a)
	{
		n.push_back (a);
	}

	for (int i (0); i < n.size () / 2; i++)
	{
		swap (n[i], n[n.size () - i - 1]);
	}

	for (int i (0); i < n.size (); i++)
	{
		cout << n[i] << ' ';
	}

	return 0;
}
'''
task3165c = '''
#include <iostream>
#include <vector>

using namespace std;

int main ()
{
	vector<int> n;
	int a;

	while (cin >> a)
	{
		n.push_back (a);
	}

	for (int i (1); i < n.size (); i += 2)
	{
		swap (n[i], n[i - 1]);
	}

	for (int i (0); i < n.size (); i++)
	{
		cout << n[i] << ' ';
	}

	return 0;
}
'''
task3166c = '''
#include <iostream>
#include <vector>

using namespace std;

int main ()
{
	vector<int> n;
	int a;

	while (cin >> a)
	{
		n.push_back (a);
	}

	a = n[0];
	for (int i (1); i < n.size (); i++)
	{
		swap (a, n[i]);
	}
	swap (a, n[0]);

	for (int i (0); i < n.size (); i++)
	{
		cout << n[i] << ' ';
	}

	return 0;
}
'''
task3167c = '''
#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int main ()
{
	vector<int> n;
	int a;
	pair<int, int> min (-1, INT_MAX), max (-1, INT_MIN);

	for (int i (0); cin >> a; i++)
	{
		n.push_back (a);

		if (a < min.second)
		{
			min.second = a;
			min.first = i;
		}

		if (a > max.second)
		{
			max.second = a;
			max.first = i;
		}
	}

	swap (n[min.first], n[max.first]);

	for (int i (0); i < n.size (); i++)
	{
		cout << n[i] << ' ';
	}

	return 0;
}
'''
task3168c = '''
#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main ()
{
	string line;
	getline (cin, line);

	int k;
	cin >> k;

	stringstream ss (line);
	for (int i (0), a; ss >> a; i++)
	{
		if (i != k)
		{
			cout << a << ' ';
		}
	}

	return 0;
}
'''
task3169c = '''
#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main ()
{
	string line;
	getline (cin, line);

	int k, c, i (0);
	cin >> k >> c;

	stringstream ss (line);

	for (int a; ss >> a; i++)
	{
		if (i == k)
		{
			cout << c << ' ';
		}

		cout << a << ' ';
	}

	if (i == k)
	{
		cout << c << ' ';
	}

	return 0;
}
'''
task317c = '''
#include <iostream>

using namespace std;

int factorial (int n)
{
	return (n == 0) ? 1 : n * factorial (n - 1);
}

int main ()
{
	int n, k;
	cin >> n >> k;

	cout << factorial (n) / (factorial (k) * factorial (n - k));

	return 0;
}
'''
task3170c = '''
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main ()
{
	vector<int> n;

	for (int a; cin >> a;)
	{
		n.push_back (a);
	}

	sort (n.begin (), n.end ());

	int prev (n[0]), equals (1), result (0);
	for (int i (1); i < n.size (); i++)
	{
		if (n[i] != prev)
		{
			result += equals * (equals - 1) / 2;
			equals = 0;
			prev = n[i];
		}
		equals++;
	}
	result += equals * (equals - 1) / 2;

	cout << result;

	return 0;
}
'''
task3171c = '''
#include <iostream>
#include <vector>

using namespace std;

int main ()
{
	vector<int> n;

	for (int a; cin >> a;)
	{
		n.push_back (a);
	}

	bool uniq;
	for (int i (0); i < n.size (); i++)
	{
		uniq = true;
		for (int j (0); j < n.size (); j++)
		{
			if ((i != j) && (n[i] == n[j]))
			{
				uniq = false;
				break;
			}
		}

		if (uniq)
		{
			cout << n[i] << ' ';
		}
	}

	return 0;
}
'''
task3172c = '''
#include <iostream>
#include <set>

using namespace std;

int main ()
{
	set<int> n;

	for (int a; cin >> a;)
	{
		n.insert (a);
	}

	cout << n.size ();

	return 0;
}
'''
task3173c = '''
#include <iostream>
#include <vector>

using namespace std;

int main ()
{
	vector<int> n;

	for (int a; cin >> a;)
	{
		n.push_back (a);
	}

	pair<int, int> result (0, 0);
	for (int i (0); i < n.size (); i++)
	{
		int count (1);
		for (int j (i + 1); j < n.size (); j++)
		{
			if (n[i] == n[j])
			{
				count++;
			}
		}

		if (count > result.second)
		{
			result.first = n[i];
			result.second = count;
		}
	}

	cout << result.first;

	return 0;
}
'''
task3174c = '''
#include <iostream>
#include <vector>

using namespace std;

int main ()
{
	vector<int> n;

	for (int a; cin >> a;)
	{
		n.push_back (a);
	}
	
	int zeroCount (0);
	for (int i (0); i < n.size (); i++)
	{
		if (!n[i])
		{
			zeroCount++;
		} else if (zeroCount)
		{
			n[i - zeroCount] = n[i];
			n[i] = 0;
		}
	}

	for (int i : n)
	{
		cout << i << ' ';
	}

	return 0;
}
'''
task3175c = '''
#include <iostream>
#include <vector>

using namespace std;

int main ()
{
	int n, k;
	cin >> n >> k;

	vector<bool> data (n, true);

	for (int i (0); i < k; i++)
	{
		int l, r;
		cin >> l >> r;

		for (int j (l - 1); j < r; j++)
		{
			data[j] = false;
		}
	}

	for (bool c : data)
	{
		cout << (c ? 'I' : '.');
	}

	return 0;
}
'''
task3176c = '''
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main ()
{
	vector<pair<int, int>> data (8);

	for (int i (0); i < 8; i++)
	{
		int x, y;
		cin >> x >> y;
		data[i] = make_pair (x, y);
	}

	bool result (false);
	for (int i (0); i < 8; i++)
	{
		for (int j (i + 1); j < 8; j++)
		{
			if ((data[i].first == data[j].first) || (data[i].second == data[j].second) || (abs (data[i].first - data[j].first) == abs (data[i].second - data[j].second)))
			{
				result = true;
				break;
			}
		}
	}

	cout << (result ? "YES" : "NO");

	return 0;
}
'''
task3177c = '''
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

int main ()
{
	string line;
	getline (cin, line);

	stringstream ss (line);

	vector<int> arr;
	for (int i (0), a; ss >> a; i++)
	{
		arr.push_back (a);
	}

	int k;
	cin >> k;
	k %= (int) arr.size ();

	rotate (arr.begin (), ((k > 0) ? arr.end () : arr.begin ()) - k, arr.end ());

	for (int nn : arr)
	{
		cout << nn << ' ';
	}

	return 0;
}
'''
task319c = '''
#include <iostream>

using namespace std;

int main ()
{
	float a;
	int n;
	cin >> a >> n;

	float result (1);
	float pow (a);
	for (int i (0); i < n; i++)
	{
		result += pow;
		pow *= a;
	}

	cout << result;

	return 0;
}
'''
task320c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	double result (1);
	for (int i (2); i <= n; i++)
	{
		result += 1. / ((long long) i * i);
	}

	cout << result;

	return 0;
}
'''
task321c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	double result (1);
	int sign (-1);
	for (int i (1); i <= n; i++)
	{
		result += sign / (double) (2 * i + 1);
		sign = -sign;
	}

	cout << 4 * result;

	return 0;
}
'''
task323c = '''
#include <iostream>

using namespace std;

struct Point
{
	int x, y;
};

int main ()
{
	int n;
	cin >> n;

	Point points[100];

	for (int i (0); i < n; i++)
	{
		int x, y;
		cin >> x >> y;
		
		points[i] = Point {x, y};
	}

	double xx (0), yy (0);
	for (int i (0); i < n; i++)
	{
		xx += points[i].x;
		yy += points[i].y;
	}

	cout << xx / n << ' ' << yy / n;

	return 0;
}
'''
task324c = '''
#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

struct Point
{
	int x, y;
};

int main ()
{
	int n;
	cin >> n;

	Point points[100];

	for (int i (0); i < n; i++)
	{
		int x, y;
		cin >> x >> y;
		
		points[i] = Point {x, y};
	}

	double maxDistance (0);
	for (int i (0); i < n; i++)
	{
		for (int j (i + 1); j < n; j++)
		{
			double curDistance = sqrt (pow (points[i].x - points[j].x, 2) + pow (points[i].y - points[j].y, 2));
			maxDistance = max (curDistance, maxDistance);
		}
	}

	cout.precision (15);
	cout << maxDistance;

	return 0;
}
'''
task325c = '''
#include <iostream>
#include <algorithm>

using namespace std;

struct Point
{
	int x, y;
};

bool compare (Point p1, Point p2)
{
	return (p1.x * p1.x + p1.y * p1.y < p2.x * p2.x + p2.y * p2.y);
}

int main ()
{
	int n;
	cin >> n;

	Point points[100];

	for (int i (0); i < n; i++)
	{
		int x, y;
		cin >> x >> y;
		
		points[i] = Point {x, y};
	}

	sort (points, points + n, compare);

	for (int i (0); i < n; i++)
	{
		cout << points[i].x << ' ' << points[i].y << endl;
	}

	return 0;
}
'''
task326c = '''
#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

struct Point
{
	int x, y;

	double distance (Point p)
	{
		return sqrt (pow (x - p.x, 2) + pow (y - p.y, 2));
	}
};

int main ()
{
	int n;
	cin >> n;

	Point points[100];

	for (int i (0); i < n; i++)
	{
		int x, y;
		cin >> x >> y;
		
		points[i] = Point {x, y};
	}

	double result (0);
	for (int i (0); i < n; i++)
	{
		for (int j (i + 1); j < n; j++)
		{
			for (int k (j + 1); k < n; k++)
			{
				double a (points[i].distance (points[j]));
				double b (points[j].distance (points[k]));
				double c (points[i].distance (points[k]));

				result = max (a + b + c, result);
			}
		}
	}

	cout.precision (15);
	cout << result;

	return 0;
}
'''
task327c = '''
#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

struct Point
{
	int x, y;

	double distance (Point p)
	{
		return sqrt (pow (x - p.x, 2) + pow (y - p.y, 2));
	}
};

int main ()
{
	int n;
	cin >> n;

	Point points[100];

	for (int i (0); i < n; i++)
	{
		int x, y;
		cin >> x >> y;
		
		points[i] = Point {x, y};
	}

	double result (0);
	for (int i (0); i < n; i++)
	{
		for (int j (i + 1); j < n; j++)
		{
			for (int k (j + 1); k < n; k++)
			{
				double a (points[i].distance (points[j]));
				double b (points[j].distance (points[k]));
				double c (points[i].distance (points[k]));

				double p ((a + b + c) / 2);

				result = max (sqrt (p * (p - a) * (p - b) * (p - c)), result);
			}
		}
	}

	cout.precision (15);
	cout << result;

	return 0;
}
'''
task328c = '''
#include <iostream>
#include <string>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	int sa (0), sb (0), sc (0);
	for (int i (0); i < n; i++)
	{
		string i1, i2;
		int a, b, c;
		cin >> i1 >> i2 >> a >> b >> c;

		sa += a;
		sb += b;
		sc += c;
	}


	cout << sa / (float) n << ' ' << sb / (float) n << ' ' << sc / (float) n;

	return 0;
}
'''
task329c = '''
#include <iostream>
#include <string>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	for (int i (0); i < n; i++)
	{
		string surname, name;
		int a, b, c;
		cin >> surname >> name >> a >> b >> c;

		if ((a > 3) && (b > 3) && (c > 3))
		{
			cout << surname << ' ' << name << endl;
		}
	}

	return 0;
}
'''
task330c = '''
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct Student
{
	string surname, name;
	int m;
};

bool compare (Student s1, Student s2)
{
	return (s1.m > s2.m);
}

int main ()
{
	int n;
	cin >> n;

	vector<Student> students;
	for (int i (0); i < n; i++)
	{
		string surname, name;
		int a, b, c;
		cin >> surname >> name >> a >> b >> c;

		students.push_back (Student {surname, name, a + b + c});
	}

	stable_sort (students.begin (), students.end (), compare);

	for (Student s : students)
	{
		if (s.m == students[0].m)
		{
			cout << s.surname << ' ' << s.name << endl;
		} else
		{
			break;
		}
	}

	return 0;
}
'''
task331c = '''
#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct Student
{
	string surname, name;
	int m;
};

int main ()
{
	int n;
	cin >> n;

	vector<Student> students;
	int m1 (0), m2 (0), m3 (0);
	for (int i (0); i < n; i++)
	{
		string surname, name;
		int a, b, c;
		cin >> surname >> name >> a >> b >> c;

		int mark (a + b + c);
		students.push_back (Student {surname, name, mark});

		if (mark > m1)
		{
			m3 = m2;
			m2 = m1;
			m1 = mark;
		} else if (mark > m2)
		{
			m3 = m2;
			m2 = mark;
		} else if (mark > m3)
		{
			m3 = mark;
		}
	}

	for (Student s : students)
	{
		if (s.m >= m3)
		{
			cout << s.surname << ' ' << s.name << endl;
		}
	}

	return 0;
}
'''
task332c = '''
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct Student
{
	string surname, name;
	int m;
};

bool compare (Student s1, Student s2)
{
	return (s1.m > s2.m);
}

int main ()
{
	int n;
	cin >> n;

	vector<Student> students;
	for (int i (0); i < n; i++)
	{
		string surname, name;
		int a, b, c;
		cin >> surname >> name >> a >> b >> c;

		students.push_back (Student {surname, name, a + b + c});
	}

	stable_sort (students.begin (), students.end (), compare);

	for (Student s : students)
	{
		cout << s.surname << ' ' << s.name << endl;
	}

	return 0;
}
'''
task333c = '''
#include <iostream>

using namespace std;

int main ()
{
	int a, b;
	cin >> a >> b;

	for (int i (a + a % 2); i <= b; i += 2)
	{
		cout << i << ' ';
	}

	return 0;
}
'''
task334c = '''
#include <iostream>

using namespace std;

int main ()
{
	int a, b, c, d;
	cin >> a >> b >> c >> d;

	for (int i (a); i <= b; i++)
	{
		if (i % d == c)
		{
			cout << i << ' ';
		}
	}

	return 0;
}
'''
task335c = '''
#include <iostream>
#include <cmath>

using namespace std;

int main ()
{
	int a, b;
	cin >> a >> b;

	int sb (sqrt (b));
	for (int i (ceil (sqrt (a))); i <= sb; i++)
	{
		cout << i * i << ' ';
	}

	return 0;
}
'''
task337c = '''
#include <iostream>

using namespace std;

int main ()
{
    int n;
    cin >> n;

    int sum (0);
    for (; n; sum += n % 10, n /= 10);

    cout << sum;

    return 0;
}
'''
task339c = '''
#include <iostream>

using namespace std;

int main ()
{
	int x;
	cin >> x;

	for (int i (2); i <= x; i++)
	{
		if (!(x % i))
		{
			cout << i;
			break;
		}
	}

	return 0;
}
'''
task340c = '''
#include <iostream>

using namespace std;

int main ()
{
	int x;
	cin >> x;

	for (int i (1); i <= x; i++)
	{
		if (!(x % i))
		{
			cout << i << ' ';
		}
	}

	return 0;
}
'''
task341c = '''
#include <iostream>
#include <cmath>

using namespace std;

int main ()
{
	int x;
	cin >> x;

	int result (0);
	for (int i (1); i <= sqrt (x); i++)
	{
		if (!(x % i))
		{
			result += 1 + (i != x / i);
		}
	}

	cout << result;

	return 0;
}
'''
task342c = '''
#include <iostream>

using namespace std;

int main ()
{
	int result (0);
	for (int i (0); i < 100; i++)
	{
		int a;
		cin >> a;

		result += a;
	}

	cout << result;

	return 0;
}
'''
task343c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	int result (0);
	for (int i (0); i < n; i++)
	{
		int a;
		cin >> a;

		result += a;
	}

	cout << result;

	return 0;
}
'''
task345c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	int result (0);
	for (int i (0); i < n; i++)
	{
		int a;
		cin >> a;

		if (!a)
		{
			result++;
		}
	}

	cout << result;

	return 0;
}
'''
task3453c = '''
#include <iostream>
#include <set>
#include <string>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	set<int> data;
	for (int i (0); i < n; i++)
	{
		string cmd;
		int a;
		cin >> cmd;
		if (cmd == "ADD")
		{
			cin >> a;
			data.insert (a);
		} else if (cmd == "PRESENT")
		{
			cin >> a;
			cout << ((data.find (a) != data.end ()) ? "YES" : "NO") << endl;
		} else
		{
			cout << data.size () << endl;
		}
	}

	return 0;
}
'''
task346c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	int neg (0), zero (0), pos (0);
	for (int i (0); i < n; i++)
	{
		int a;
		cin >> a;

		if (!a)
		{
			zero++;
		} else if (a > 0)
		{
			pos++;
		} else
		{
			neg++;
		}
	}

	cout << zero << ' ' << pos << ' ' << neg;

	return 0;
}
'''
task347c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	for (int i (0); i < n; i++)
	{
		int a;
		cin >> a;

		if (!a)
		{
			cout << "YES";
			return 0;
		}
	}

	cout << "NO";

	return 0;
}
'''
task348c = '''
#include <iostream>

using namespace std;

int main ()
{
	int a, b, c, d;
	cin >> a >> b >> c >> d;

	for (int i (0); i <= 1000; i++)
	{
		int ii (i * i);
		if (a * i * ii + b * ii + c * i == -d)
		{
			cout << i << ' ';
		}
	}

	return 0;
}
'''
task349c = '''
#include <iostream>

using namespace std;

int main ()
{
	int a, b, c, d;
	cin >> a >> b >> c >> d;

	for (int i (1000); i >= 0; i--)
	{
		int ii (i * i);
		if (a * i * ii + b * ii + c * i == -d)
		{
			cout << i << ' ';
		}
	}

	return 0;
}
'''
task350c = '''
#include <iostream>

using namespace std;

int main ()
{
	int a, b, c, d, e;
	cin >> a >> b >> c >> d >> e;

	int result (0);
	for (int i (0); i <= 1000; i++)
	{
		int ii (i * i);
		if ((i - e) && (!(a * i * ii + b * ii + c * i + d)))
		{
			result++;
		}
	}

	cout << result;

	return 0;
}
'''
task351c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	int result (1);
	for (int i (2); i <= n; i++)
	{
		result *= i;
	}

	cout << result;

	return 0;
}
'''
task352c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	int result (1);
	for (int i (1); i <= n; i++)
	{
		result *= 2;
	}

	cout << result;

	return 0;
}
'''
task3528c = '''
#include <iostream>

using namespace std;

int main ()
{
    int a, b;
    cin >> a >> b;

    for (int i (a); i <= b; i++)
    {
        cout << i << ' ';
    }

    return 0;
}
'''
task3529c = '''
#include <iostream>

using namespace std;

int main ()
{
    int a, b;
    cin >> a >> b;

    if (a <= b)
    {
        for (int i (a); i <= b; i++)
        {
            cout << i << ' ';
        }
    } else
    {
        for (int i (a); i >= b; i--)
        {
            cout << i << ' ';
        }
    }

    return 0;
}
'''
task353c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	int result (1);
	int pow2 (2);
	for (int i (1); i <= n; i++)
	{
		result += pow2;
		pow2 *= 2;
	}

	cout << result;

	return 0;
}
'''
task3530c = '''
#include <iostream>
#include <cmath>

using namespace std;

int main ()
{
    int n;
    cin >> n;

    for (int i (pow (10, n) - 1); i >= pow (10, n - 1); i -= 2)
    {
        cout << i << ' ';
    }

    return 0;
}
'''
task3535c = '''
#include <iostream>

using namespace std;

int main ()
{
    int n;
    cin >> n;

    char image[5][11] =
    {
        "   _~_    ",
        "  (o o)   ",
        " /  V  \\  ",
        "/(  _  )\\ ",
        "  ^^ ^^   "
    };

    for (int i (0); i < 5; i++)
    {
        for (int j (0); j < n; j++)
        {
            cout << image[i];
        }

        cout << endl;
    }

    return 0;
}
'''
task3536c = '''
#include <iostream>

using namespace std;

int main ()
{
    int n;
    cin >> n;

    char image[4][6] =
    {
        "+___ ",
        "|N / ",
        "|__\\ ",
        "|    "
    };

    for (int i (0); i < 4; i++)
    {
        for (int j (0); j < n; j++)
        {
            for (int k (0); k < 5; k++)
            {
                cout << ((image[i][k] == 'N') ? (char) ('1' + j) : image[i][k]);
            }
        }

        cout << endl;
    }

    return 0;
}
'''
task3544c = '''
#include <iostream>

using namespace std;

int main ()
{
    for (int i (10); i <= 99; i++)
    {
        int m (1);
        for (int l (i); l; m *= l % 10, l /= 10);

        if (m * 2 == i)
        {
            cout << i << endl;
        }
    }

    return 0;
}
'''
task3546c = '''
#include <iostream>

using namespace std;

int main ()
{
    int n;
    cin >> n;

    for (int i (100); i <= 999; i++)
    {
        int sum (0);
        for (int l (i); l; sum += l % 10, l /= 10);

        if (sum == n)
        {
            cout << i << endl;
        }
    }

    return 0;
}
'''
task3548c = '''
#include <iostream>

using namespace std;

bool isPalindrome (int n)
{
    return ((n / 1000 == n % 10) && (n / 10 % 10 == n / 100 % 10));
}

int main ()
{
    int a, b;
    cin >> a >> b;

    for (int i (a); i <= b; i++)
    {
        if (isPalindrome (i))
        {
            cout << i << endl;
        }
    }

    return 0;
}
'''
task355c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n;
	cin >> n;

	int arr[100][100];
	for (int i (0); i < n; i++)
	{
		for (int j (0); j < n; j++)
		{
			cin >> arr[i][j];
		}
	}

	for (int i (0); i < n; i++)
	{
		for (int j (i); j < n; j++)
		{
			if (arr[i][j] != arr[j][i])
			{
				cout << "no";
				return 0;
			}
		};
	}

	cout << "yes";

	return 0;
}
'''
task356c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n, m;
	cin >> n >> m;

	int maxSum (0), ind (0);
	for (int i (0); i < n; i++)
	{
		int curSum (0);
		for (int j (0), a; j < m; j++)
		{
			cin >> a;
			curSum += a;
		}

		if (curSum > maxSum)
		{
			maxSum = curSum;
			ind = i;
		}
	}

	cout << maxSum << endl << ind;

	return 0;
}
'''
task357c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n, m;
	cin >> n >> m;

	int max (0), x (0), y (0);
	for (int i (0); i < n; i++)
	{
		for (int j (0), a; j < m; j++)
		{
			cin >> a;

			if (a > max)
			{
				max = a;
				x = i;
				y = j;
			}
		}
	}

	cout << max << endl << x << ' ' << y;

	return 0;
}
'''
task358c = '''
#include <iostream>
#include <algorithm>

using namespace std;

struct Sportsman
{
	int id, bestTry, totalScore;
};

bool comparator (Sportsman s1, Sportsman s2)
{
	if (s1.bestTry == s2.bestTry)
	{
		if (s1.totalScore == s2.totalScore)
		{
			return (s1.id < s1.id);
		}

		return (s1.totalScore > s2.totalScore);
	}

	return (s1.bestTry > s2.bestTry);
}

int main ()
{
	int n, m;
	cin >> n >> m;

	Sportsman* arr = new Sportsman[n];
	for (int i (0); i < n; i++)
	{
		arr[i].id = i;
		arr[i].bestTry = 0;
		arr[i].totalScore = 0;

		for (int j (0), a; j < m; j++)
		{
			cin >> a;
			arr[i].totalScore += a;

			if (a > arr[i].bestTry)
			{
				arr[i].bestTry = a;
			}
		}
	}

	sort (arr, arr + n, comparator);

	cout << arr[0].id;

	return 0;
}
'''
task359c = '''
#include <iostream>
#include <algorithm>

using namespace std;

bool comparator (int n1, int n2)
{
	return n1 > n2;
}

int main ()
{
	int n, m;
	cin >> n >> m;

	int* arr = new int[n];
	for (int i (0); i < n; i++)
	{
		arr[i] = 0;

		for (int j (0), a; j < m; j++)
		{
			cin >> a;

			if (a > arr[i])
			{
				arr[i] = a;
			}
		}
	}

	sort (arr, arr + n, comparator);

	int result (1);
	for (int i (1); i < n; i++)
	{
		if (arr[i] != arr[0])
		{
			break;
		}

		result++;
	}

	cout << result;

	return 0;
}
'''
task360c = '''
#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;

int comparator (pair<int, int> s1, pair<int, int> s2)
{
	if (s1.second == s2.second)
	{
		return s1.first < s2.first;
	}

	return s1.second > s2.second;
}

int main ()
{
	vector<pair<int, int>> data;

	int n, m;
	cin >> n >> m;

	for (int i (0); i < n; i++)
	{
		int mx, a;
		cin >> mx;
		for (int j (1); j < m; j++)
		{
			cin >> a;
			mx = max (mx, a);
		}

		data.push_back (make_pair (i, mx));
	}

	sort (data.begin (), data.end (), comparator);

	stringstream ind;
	int result (0);
	for (; ((result < n) && (data[result].second == data[0].second)); result++)
	{
		ind << data[result].first << ' ';
	}

	cout << result << endl << ind.str ();

	return 0;
}
'''
task361c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n, m;
	cin >> n >> m;

	int** arr = new int* [n];
	for (int k (0); k < n * m; k++)
	{
		int i = k / m;
		int j = k % m;

		if (!j)
		{
			arr[i] = new int[m];
		}
		arr[i][j] = i * j;
	}

	for (int i (0); i < n; i++)
	{
		for (int j (0); j < m; j++)
		{
			cout << arr[i][j] << ' ';
		}
		cout << endl;
	}

	return 0;
}
'''
task362c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n, m;
	cin >> n >> m;

	int** arr = new int* [n];
	for (int i (0); i < n; i++)
	{
		arr[i] = new int[m];

		for (int j (0); j < m; j++)
		{
			arr[i][j] = (((!i) || (!j)) ? 1 : arr[i - 1][j] + arr[i][j - 1]);
		}
	}

	for (int i (0); i < n; i++)
	{
		for (int j (0); j < m; j++)
		{
			cout << arr[i][j] << ' ';
		}
		cout << endl;
	}

	return 0;
}
'''
task363c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n, m;
	cin >> n >> m;

	int** arr = new int* [n];
	for (int i (0); i < n; i++)
	{
		arr[i] = new int[m];

		int limit ((i + 1) * m - 1);
		for (int j (0); j < m; j++)
		{
			arr[i][j] = ((i % 2) ? limit - j : limit - m + j + 1);
		}
	}

	for (int i (0); i < n; i++)
	{
		for (int j (0); j < m; j++)
		{
			cout.width (3);
			cout << arr[i][j] << ' ';
		}
		cout << endl;
	}

	return 0;
}
'''
task264c = '''
#include <iostream>

using namespace std;

int main ()
{
	int n, m;
	cin >> n >> m;

	int** arr = new int* [n];
	for (int i (0); i < n; i++)
	{
		arr[i] = new int[m];
	}

	for (int j (0), el (0); j < m + n - 1; j++)
	{ 
		for (int i (0); ((i <= j) && (i < n)); i++)
		{
			if (j - i < m)
			{
				arr[i][j - i] = el++;
			}
		}
	}

	for (int i (0); i < n; i++)
	{
		for (int j (0); j < m; j++)
		{
			cout.width (3);
			cout << arr[i][j] << ' ';
		}
		cout << endl;
	}

	return 0;
}
'''
@bot.message_handler(commands=["start"])
def starts(message):
    bot.send_message(message.chat.id, "Хочешь посмотреть решение задач по информатике?", reply_markup=virkey)

@bot.message_handler(commands=["помощь"])
def helps(message):
    bot.send_message(message.chat.id, Help)

@bot.message_handler(commands=["язык"])
def langs(message):
	bot.send_message(message.chat.id, "для того, чтобы узнать решение задач с informatics.msk напишите: task(номер)py - питон / task(номер)c - с++")  #reply_markup=langkey
#def otvet(message):
#   if message.text.lower() == '/С++':
 #     bot.send_message(message.chat.id, "для того, чтобы узнать решение задач с informatics.msk напишите: task(номер)py - питон / task(номер)c - с++")
 #  elif message.text.lower() == '/Python':
  #    bot.send_message(message.chat.id, "для того, чтобы узнать решение задач с informatics.msk напишите: task(номер)py - питон / task(номер)c - с++")




@bot.message_handler(commands=["пока"])
def goodbuy(message):
    bot.send_message(message.chat.id, "пока, незнакомец!")
    bot.polling(stop = True)

@bot.message_handler(content_types=["text"])
def eho(message):
    if message.text.lower() == 'да':
	    bot.send_message(message.chat.id, "для того, чтобы узнать решение задач с informatics.msk напишите: task(номер)py - питон / task(номер)c - с++")
    elif message.text.lower() == 'нет':
	    bot.send_message(message.chat.id, "чем еще можем помочь?")
    elif message.text.lower() == 'task102c':
        bot.send_message(message.chat.id, task102c)
    elif message.text.lower() == 'task1023c':
        bot.send_message(message.chat.id, task1023c)
    elif message.text.lower() == 'task103c':
        bot.send_message(message.chat.id, task103c)
    elif message.text.lower() == 'task104c':
        bot.send_message(message.chat.id, task104c)
    elif message.text.lower() == 'task105c':
        bot.send_message(message.chat.id, task105c)
    elif message.text.lower() == 'task106c':
        bot.send_message(message.chat.id, task106c) 
    elif message.text.lower() == 'task107c':
        bot.send_message(message.chat.id, task107c)
    elif message.text.lower() == 'task108c':
        bot.send_message(message.chat.id, task108c) 
    elif message.text.lower() == 'task109c':
        bot.send_message(message.chat.id, task109c) 
    elif message.text.lower() == 'task110c':
        bot.send_message(message.chat.id, task110c) 
    elif message.text.lower() == 'task111c':
        bot.send_message(message.chat.id, task111c)
    elif message.text.lower() == 'task111642c':
        bot.send_message(message.chat.id, task111642c)
    elif message.text.lower() == 'task111660c':
        bot.send_message(message.chat.id, task111660c) 
    elif message.text.lower() == 'task111668c':
        bot.send_message(message.chat.id, task111668c) 
    elif message.text.lower() == 'task111670c':
        bot.send_message(message.chat.id, task112c)
    elif message.text.lower() == 'task112c':
        bot.send_message(message.chat.id, task112c)
    elif message.text.lower() == 'task112145c':
        bot.send_message(message.chat.id, task112145c) 
    elif message.text.lower() == 'task112147c':
        bot.send_message(message.chat.id, task112147c)
    elif message.text.lower() == 'task112161c':
        bot.send_message(message.chat.id, task112161c)
    elif message.text.lower() == 'task112162c':
        bot.send_message(message.chat.id, task112162c) 
    elif message.text.lower() == 'task113c':
        bot.send_message(message.chat.id, task113c) 
    elif message.text.lower() == 'task113652c':
        bot.send_message(message.chat.id, task113652c) 
    elif message.text.lower() == 'task113653c':
        bot.send_message(message.chat.id, task113653c) 
    elif message.text.lower() == 'task113654c':
        bot.send_message(message.chat.id, task113654c) 
    elif message.text.lower() == 'task113655c':
        bot.send_message(message.chat.id, task113655c) 
    elif message.text.lower() == 'task113656c':
        bot.send_message(message.chat.id, task113656c) 
    elif message.text.lower() == 'task113657c':
        bot.send_message(message.chat.id, task113657c) 
    elif message.text.lower() == 'task113658c':
        bot.send_message(message.chat.id, task113658c) 
    elif message.text.lower() == 'task113659c':
        bot.send_message(message.chat.id, task113659c) 
    elif message.text.lower() == 'task114c':
        bot.send_message(message.chat.id, task114c)
    elif message.text.lower() == 'task115c':
        bot.send_message(message.chat.id, task115c) 
    elif message.text.lower() == 'task116c':
        bot.send_message(message.chat.id, task116c) 
    elif message.text.lower() == 'task117c':
        bot.send_message(message.chat.id, task117c) 
    elif message.text.lower() == 'task11764c':
        bot.send_message(message.chat.id, task11764c) 
    elif message.text.lower() == 'task118c':
        bot.send_message(message.chat.id, task118c) 
    elif message.text.lower() == 'task119c':
        bot.send_message(message.chat.id, task119c)
    elif message.text.lower() == 'task120c':
        bot.send_message(message.chat.id, task120c)
    elif message.text.lower() == 'task121c':
        bot.send_message(message.chat.id, task121c)
    elif message.text.lower() == 'task122c':
        bot.send_message(message.chat.id, task122c) 
    elif message.text.lower() == 'task123c':
        bot.send_message(message.chat.id, task123c) 
    elif message.text.lower() == 'task124c':
        bot.send_message(message.chat.id, task124c) 
    elif message.text.lower() == 'task125c':
        bot.send_message(message.chat.id, task125c) 
    elif message.text.lower() == 'task126c':
        bot.send_message(message.chat.id, task126c) 
    elif message.text.lower() == 'task127c':
        bot.send_message(message.chat.id, task127c) 
    elif message.text.lower() == 'task128c':
        bot.send_message(message.chat.id, task128c) 
    elif message.text.lower() == 'task129c':
        bot.send_message(message.chat.id, task129c)
    elif message.text.lower() == 'task1404c':
        bot.send_message(message.chat.id, task1404c) 
    elif message.text.lower() == 'task1415c':
        bot.send_message(message.chat.id, task1415c)
    elif message.text.lower() == 'task1417c':
        bot.send_message(message.chat.id, task1417c) 
    elif message.text.lower() == 'task1418c':
        bot.send_message(message.chat.id, task1418c)
    elif message.text.lower() == 'task1421c':
        bot.send_message(message.chat.id, task1421c)
    elif message.text.lower() == 'task1430c':
        bot.send_message(message.chat.id, task1430c)
    elif message.text.lower() == 'task1433c':
        bot.send_message(message.chat.id, task1433c) 
    elif message.text.lower() == 'task1435c':
        bot.send_message(message.chat.id, task1435c) 
    elif message.text.lower() == 'task1444c':
        bot.send_message(message.chat.id, task1444c) 
    elif message.text.lower() == 'task1445c':
        bot.send_message(message.chat.id, task1445c) 
    elif message.text.lower() == 'task1448c':
        bot.send_message(message.chat.id, task1448c) 
    elif message.text.lower() == 'task1450c':
        bot.send_message(message.chat.id, task1450c) 
    elif message.text.lower() == 'task1451c':
        bot.send_message(message.chat.id, task1451c) 
    elif message.text.lower() == 'task1456c':
        bot.send_message(message.chat.id, task1456c) 
    elif message.text.lower() == 'task1457c':
        bot.send_message(message.chat.id, task1458c) 
    elif message.text.lower() == 'task1459c':
        bot.send_message(message.chat.id, task1459c) 
    elif message.text.lower() == 'task1460c':
        bot.send_message(message.chat.id, task1460c)
    elif message.text.lower() == 'task1461c':
        bot.send_message(message.chat.id, task1461c) 
    elif message.text.lower() == 'task1464c':
        bot.send_message(message.chat.id, task1464c) 
    elif message.text.lower() == 'task1466c':
        bot.send_message(message.chat.id, task1466c) 
    elif message.text.lower() == 'task1467c':
        bot.send_message(message.chat.id, task1467c) 
    elif message.text.lower() == 'task1468c':
        bot.send_message(message.chat.id, task1468c) 
    elif message.text.lower() == 'task1475c':
        bot.send_message(message.chat.id, task1475c) 
    elif message.text.lower() == 'task1476c':
        bot.send_message(message.chat.id, task1476c) 
    elif message.text.lower() == 'task1479c':
        bot.send_message(message.chat.id, task1479c) 
    elif message.text.lower() == 'task1483c':
        bot.send_message(message.chat.id, task1483c) 
    elif message.text.lower() == 'task201c':
        bot.send_message(message.chat.id, task201c)
    elif message.text.lower() == 'task203c':
        bot.send_message(message.chat.id, task203c) 
    elif message.text.lower() == 'task208c':
        bot.send_message(message.chat.id, task208c) 
    elif message.text.lower() == 'task234c':
        bot.send_message(message.chat.id, task234c) 
    elif message.text.lower() == 'task236c':
        bot.send_message(message.chat.id, task236c) 
    elif message.text.lower() == 'task238c':
        bot.send_message(message.chat.id, task238c)
    elif message.text.lower() == 'task243c':
        bot.send_message(message.chat.id, task243c) 
    elif message.text.lower() == 'task247c':
        bot.send_message(message.chat.id, task247c) 
    elif message.text.lower() == 'task252c':
        bot.send_message(message.chat.id, task252c) 
    elif message.text.lower() == 'task253c':
        bot.send_message(message.chat.id, task253c) 
    elif message.text.lower() == 'task254c':
        bot.send_message(message.chat.id, task254c) 
    elif message.text.lower() == 'task255c':
        bot.send_message(message.chat.id, task255c) 
    elif message.text.lower() == 'task256c':
        bot.send_message(message.chat.id, task256c) 
    elif message.text.lower() == 'task257c':
        bot.send_message(message.chat.id, task257c) 
    elif message.text.lower() == 'task258c':
        bot.send_message(message.chat.id, task258c) 
    elif message.text.lower() == 'task259c':
        bot.send_message(message.chat.id, task260c) 
    elif message.text.lower() == 'task261c':
        bot.send_message(message.chat.id, task261c) 
    elif message.text.lower() == 'task262c':
        bot.send_message(message.chat.id, task262c) 
    elif message.text.lower() == 'task264c':
        bot.send_message(message.chat.id, task264c) 
    elif message.text.lower() == 'task265c':
        bot.send_message(message.chat.id, task265c) 
    elif message.text.lower() == 'task266c':
        bot.send_message(message.chat.id, task266c) 
    elif message.text.lower() == 'task279c':
        bot.send_message(message.chat.id, task279c) 
    elif message.text.lower() == 'task2796c':
        bot.send_message(message.chat.id, task2796c)
    elif message.text.lower() == 'task2797c':
        bot.send_message(message.chat.id, task2797c) 
    elif message.text.lower() == 'task282c':
        bot.send_message(message.chat.id, task282c) 
    elif message.text.lower() == 'task292c':
        bot.send_message(message.chat.id, task292c) 
    elif message.text.lower() == 'task293c':
        bot.send_message(message.chat.id, task293c) 
    elif message.text.lower() == 'task2936c':
        bot.send_message(message.chat.id, task2936c) 
    elif message.text.lower() == 'task2937c':
        bot.send_message(message.chat.id, task2937c) 
    elif message.text.lower() == 'task2938c':
        bot.send_message(message.chat.id, task2938c) 
    elif message.text.lower() == 'task2939c':
        bot.send_message(message.chat.id, task2939c) 
    elif message.text.lower() == 'task294c':
        bot.send_message(message.chat.id, task294c) 
    elif message.text.lower() == 'task2940c':
        bot.send_message(message.chat.id, task2940c) 
    elif message.text.lower() == 'task2941c':
        bot.send_message(message.chat.id, task2941c) 
    elif message.text.lower() == 'task2942c':
        bot.send_message(message.chat.id, task2942c) 
    elif message.text.lower() == 'task2943c':
        bot.send_message(message.chat.id, task2943c) 
    elif message.text.lower() == 'task2944c':
        bot.send_message(message.chat.id, task2944c) 
    elif message.text.lower() == 'task2945c':
        bot.send_message(message.chat.id, task2945c) 
    elif message.text.lower() == 'task2947c':
        bot.send_message(message.chat.id, task2947c) 
    elif message.text.lower() == 'task2948c':
        bot.send_message(message.chat.id, task2948c) 
    elif message.text.lower() == 'task2949c':
        bot.send_message(message.chat.id, task2949c) 
    elif message.text.lower() == 'task295c':
        bot.send_message(message.chat.id, task295c) 
    elif message.text.lower() == 'task2950c':
        bot.send_message(message.chat.id, task2950c) 
    elif message.text.lower() == 'task2951c':
        bot.send_message(message.chat.id, task2951c) 
    elif message.text.lower() == 'task2952c':
        bot.send_message(message.chat.id, task2952c) 
    elif message.text.lower() == 'task2953c':
        bot.send_message(message.chat.id, task2953c) 
    elif message.text.lower() == 'task2954c':
        bot.send_message(message.chat.id, task2954c) 
    elif message.text.lower() == 'task2956c':
        bot.send_message(message.chat.id, task2956c) 
    elif message.text.lower() == 'task2957c':
        bot.send_message(message.chat.id, task2957c) 
    elif message.text.lower() == 'task2959c':
        bot.send_message(message.chat.id, task2959c) 
    elif message.text.lower() == 'task296c':
        bot.send_message(message.chat.id, task296c) 
    elif message.text.lower() == 'task2960c':
        bot.send_message(message.chat.id, task2960c) 
    elif message.text.lower() == 'task2961c':
        bot.send_message(message.chat.id, task2961c) 
    elif message.text.lower() == 'task298c':
        bot.send_message(message.chat.id, task298c) 
    elif message.text.lower() == 'task300c':
        bot.send_message(message.chat.id, task300c) 
    elif message.text.lower() == 'task301c':
        bot.send_message(message.chat.id, task301c) 
    elif message.text.lower() == 'task302c':
        bot.send_message(message.chat.id, task302c) 
    elif message.text.lower() == 'task3024c':
        bot.send_message(message.chat.id, task3024c) 
    elif message.text.lower() == 'task303c':
        bot.send_message(message.chat.id, task303c) 
    elif message.text.lower() == 'task304c':
        bot.send_message(message.chat.id, task304c) 
    elif message.text.lower() == 'task305c':
        bot.send_message(message.chat.id, task305c) 
    elif message.text.lower() == 'task3058c':
        bot.send_message(message.chat.id, task3058c) 
    elif message.text.lower() == 'task3059c':
        bot.send_message(message.chat.id, task3059c) 
    elif message.text.lower() == 'task306c':
        bot.send_message(message.chat.id, task306c) 
    elif message.text.lower() == 'task3060c':
        bot.send_message(message.chat.id, task3060c)
    elif message.text.lower() == 'task3061c':
        bot.send_message(message.chat.id, task3061c) 
    elif message.text.lower() == 'task3062c':
        bot.send_message(message.chat.id, task3062c) 
    elif message.text.lower() == 'task3063c':
        bot.send_message(message.chat.id, task3063c) 
    elif message.text.lower() == 'task3064c':
        bot.send_message(message.chat.id, task3064c) 
    elif message.text.lower() == 'task3065c':
        bot.send_message(message.chat.id, task3065c) 
    elif message.text.lower() == 'task3066c':
        bot.send_message(message.chat.id, task3066c) 
    elif message.text.lower() == 'task3067c':
        bot.send_message(message.chat.id, task3067c) 
    elif message.text.lower() == 'task3068c':
        bot.send_message(message.chat.id, task3068c) 
    elif message.text.lower() == 'task3069c':
        bot.send_message(message.chat.id, task3069c) 
    elif message.text.lower() == 'task307c':
        bot.send_message(message.chat.id, task307c) 
    elif message.text.lower() == 'task3070c':
        bot.send_message(message.chat.id, task3070c) 
    elif message.text.lower() == 'task3071c':
        bot.send_message(message.chat.id, task3071c) 
    elif message.text.lower() == 'task3072c':
        bot.send_message(message.chat.id, task3072c) 
    elif message.text.lower() == 'task3073c':
        bot.send_message(message.chat.id, task3073c) 
    elif message.text.lower() == 'task3074c':
        bot.send_message(message.chat.id, task3074c) 
    elif message.text.lower() == 'task3075c':
        bot.send_message(message.chat.id, task3075c) 
    elif message.text.lower() == 'task3076c':
        bot.send_message(message.chat.id, task3076c) 
    elif message.text.lower() == 'task3077c':
        bot.send_message(message.chat.id, task3077c) 
    elif message.text.lower() == 'task3078c':
        bot.send_message(message.chat.id, task3078c) 
    elif message.text.lower() == 'task3079c':
        bot.send_message(message.chat.id, task3079c) 
    elif message.text.lower() == 'task308c':
        bot.send_message(message.chat.id, task308c)
    elif message.text.lower() == 'task3080c':
        bot.send_message(message.chat.id, task3080c) 
    elif message.text.lower() == 'task3081c':
        bot.send_message(message.chat.id, task3081c) 
    elif message.text.lower() == 'task3082c':
        bot.send_message(message.chat.id, task3082c) 
    elif message.text.lower() == 'task309c':
        bot.send_message(message.chat.id, task309c) 
    elif message.text.lower() == 'task310c':
        bot.send_message(message.chat.id, task310c) 
    elif message.text.lower() == 'task311c':
        bot.send_message(message.chat.id, task311c) 
    elif message.text.lower() == 'task3116c':
        bot.send_message(message.chat.id, task3116c) 
    elif message.text.lower() == 'task3117c':
        bot.send_message(message.chat.id, task3117c) 
    elif message.text.lower() == 'task3118c':
        bot.send_message(message.chat.id, task3118c) 
    elif message.text.lower() == 'task3119c':
        bot.send_message(message.chat.id, task3119c) 
    elif message.text.lower() == 'task312c':
        bot.send_message(message.chat.id, task312c) 
    elif message.text.lower() == 'task3120c':
        bot.send_message(message.chat.id, task3120c) 
    elif message.text.lower() == 'task3121c':
        bot.send_message(message.chat.id, task3121c) 
    elif message.text.lower() == 'task3122c':
        bot.send_message(message.chat.id, task3122c) 
    elif message.text.lower() == 'task3123c':
        bot.send_message(message.chat.id, task3123c) 
    elif message.text.lower() == 'task3124c':
        bot.send_message(message.chat.id, task3124c) 
    elif message.text.lower() == 'task3125c':
        bot.send_message(message.chat.id, task3125c) 
    elif message.text.lower() == 'task3126c':
        bot.send_message(message.chat.id, task3126c) 
    elif message.text.lower() == 'task3127c':
        bot.send_message(message.chat.id, task3127c) 
    elif message.text.lower() == 'task3128c':
        bot.send_message(message.chat.id, task3128c) 
    elif message.text.lower() == 'task3129c':
        bot.send_message(message.chat.id, task3129c) 
    elif message.text.lower() == 'task313c':
        bot.send_message(message.chat.id, task313c) 
    elif message.text.lower() == 'task315c':
        bot.send_message(message.chat.id, task315c)
    elif message.text.lower() == 'task3152c':
        bot.send_message(message.chat.id, task3152c) 
    elif message.text.lower() == 'task3153c':
        bot.send_message(message.chat.id, task3153c) 
    elif message.text.lower() == 'task3154c':
        bot.send_message(message.chat.id, task3154c) 
    elif message.text.lower() == 'task3155c':
        bot.send_message(message.chat.id, task3155c) 
    elif message.text.lower() == 'task3156c':
        bot.send_message(message.chat.id, task3156c) 
    elif message.text.lower() == 'task3157c':
        bot.send_message(message.chat.id, task3157c) 
    elif message.text.lower() == 'task3158c':
        bot.send_message(message.chat.id, task3158c) 
    elif message.text.lower() == 'task3159c':
        bot.send_message(message.chat.id, task3159c) 
    elif message.text.lower() == 'task316c':
        bot.send_message(message.chat.id, task316c)
    elif message.text.lower() == 'task3160c':
        bot.send_message(message.chat.id, task3160c) 
    elif message.text.lower() == 'task3161c':
        bot.send_message(message.chat.id, task3161c) 
    elif message.text.lower() == 'task3162c':
        bot.send_message(message.chat.id, task3162c) 
    elif message.text.lower() == 'task3163c':
        bot.send_message(message.chat.id, task3163c) 
    elif message.text.lower() == 'task3164c':
        bot.send_message(message.chat.id, task3164c) 
    elif message.text.lower() == 'task3165c':
        bot.send_message(message.chat.id, task3165c) 
    elif message.text.lower() == 'task3166c':
        bot.send_message(message.chat.id, task3166c) 
    elif message.text.lower() == 'task3167c':
        bot.send_message(message.chat.id, task3167c) 
    elif message.text.lower() == 'task3168c':
        bot.send_message(message.chat.id, task3168c) 
    elif message.text.lower() == 'task3169c':
        bot.send_message(message.chat.id, task3169c) 
    elif message.text.lower() == 'task317c':
        bot.send_message(message.chat.id, task317c) 
    elif message.text.lower() == 'task3170c':
        bot.send_message(message.chat.id, task3170c) 
    elif message.text.lower() == 'task3171c':
        bot.send_message(message.chat.id, task3171c) 
    elif message.text.lower() == 'task3172c':
        bot.send_message(message.chat.id, task3172c) 
    elif message.text.lower() == 'task3173c':
        bot.send_message(message.chat.id, task3173c) 
    elif message.text.lower() == 'task3174c':
        bot.send_message(message.chat.id, task3174c)  
    elif message.text.lower() == 'task3175c':
        bot.send_message(message.chat.id, task3175c) 
    elif message.text.lower() == 'task3176c':
        bot.send_message(message.chat.id, task3176c) 
    elif message.text.lower() == 'task3177c':
        bot.send_message(message.chat.id, task3177c) 
    elif message.text.lower() == 'task319c':
        bot.send_message(message.chat.id, task319c) 
    elif message.text.lower() == 'task320c':
        bot.send_message(message.chat.id, task320c) 
    elif message.text.lower() == 'task323c':
        bot.send_message(message.chat.id, task323c) 
    elif message.text.lower() == 'task324c':
        bot.send_message(message.chat.id, task324c) 
    elif message.text.lower() == 'task325c':
        bot.send_message(message.chat.id, task325c) 
    elif message.text.lower() == 'task326c':
        bot.send_message(message.chat.id, task326c) 
    elif message.text.lower() == 'task327c':
        bot.send_message(message.chat.id, task327c) 
    elif message.text.lower() == 'task328c':
        bot.send_message(message.chat.id, task328c) 
    elif message.text.lower() == 'task339c':
        bot.send_message(message.chat.id, task329c) 
    elif message.text.lower() == 'task330c':
        bot.send_message(message.chat.id, task330c)
    elif message.text.lower() == 'task331c':
        bot.send_message(message.chat.id, task331c)  
    elif message.text.lower() == 'task332c':
        bot.send_message(message.chat.id, task332c) 
    elif message.text.lower() == 'task333c':
        bot.send_message(message.chat.id, task333c) 
    elif message.text.lower() == 'task334c':
        bot.send_message(message.chat.id, task334c) 
    elif message.text.lower() == 'task335c':
        bot.send_message(message.chat.id, task335c) 
    elif message.text.lower() == 'task337c':
        bot.send_message(message.chat.id, task337c) 
    elif message.text.lower() == 'task339c':
        bot.send_message(message.chat.id, task339c)
    elif message.text.lower() == 'task340c':
        bot.send_message(message.chat.id, task340c) 
    elif message.text.lower() == 'task341c':
        bot.send_message(message.chat.id, task341c) 
    elif message.text.lower() == 'task342c':
        bot.send_message(message.chat.id, task342c) 
    elif message.text.lower() == 'task343c':
        bot.send_message(message.chat.id, task343c) 
    elif message.text.lower() == 'task345c':
        bot.send_message(message.chat.id, task345c)
    elif message.text.lower() == 'task3453c':
        bot.send_message(message.chat.id, task3453c)  
    elif message.text.lower() == 'task346c':
        bot.send_message(message.chat.id, task346c) 
    elif message.text.lower() == 'task347c':
        bot.send_message(message.chat.id, task347c) 
    elif message.text.lower() == 'task348c':
        bot.send_message(message.chat.id, task348c) 
    elif message.text.lower() == 'task349c':
        bot.send_message(message.chat.id, task349c) 
    elif message.text.lower() == 'task350c':
        bot.send_message(message.chat.id, task350c) 
    elif message.text.lower() == 'task351c':
        bot.send_message(message.chat.id, task351c) 
    elif message.text.lower() == 'task352c':
        bot.send_message(message.chat.id, task352c) 
    elif message.text.lower() == 'task3528c':
        bot.send_message(message.chat.id, task3528c) 
    elif message.text.lower() == 'task3529c':
        bot.send_message(message.chat.id, task3529c) 
    elif message.text.lower() == 'task353c':
        bot.send_message(message.chat.id, task353c) 
    elif message.text.lower() == 'task3530c':
        bot.send_message(message.chat.id, task3530c) 
    elif message.text.lower() == 'task3535c':
        bot.send_message(message.chat.id, task3535c) 
    elif message.text.lower() == 'task3536c':
        bot.send_message(message.chat.id, task3536c) 
    elif message.text.lower() == 'task3544c':
        bot.send_message(message.chat.id, task3544c) 
    elif message.text.lower() == 'task3546c':
        bot.send_message(message.chat.id, task3546c) 
    elif message.text.lower() == 'task3548c':
        bot.send_message(message.chat.id, task3548c) 
    elif message.text.lower() == 'task355c':
        bot.send_message(message.chat.id, task355c) 
    elif message.text.lower() == 'task356c':
        bot.send_message(message.chat.id, task356c) 
    elif message.text.lower() == 'task357c':
        bot.send_message(message.chat.id, task357c) 
    elif message.text.lower() == 'task358c':
        bot.send_message(message.chat.id, task358c) 
    elif message.text.lower() == 'task359c':
        bot.send_message(message.chat.id, task359c) 
    else:
       # bot.send_message(message.chat.id, message.text)                   #task(номер)py - питон / task(номер)c - с++
        bot.reply_to(message, "Такой команды я не знаю")

bot.polling(none_stop = True)
