// ConsoleApplication2.cpp: главный файл проекта.

#include "stdafx.h"
#include <iostream>
#include <string>
#include <vector>
#include <chrono>
#include <ctime>

using namespace System;
using namespace std;

int S, L, LL;
long long cntres, summ;
std::string line;
vector<int> lengths;
const char * src;

void proc(int curlen, int ll, int srclen)
{
	if (curlen == L + 1)
	{
		if (ll == 0)
			cntres++;
		return;
	}
	if (ll == 0 && curlen < L)
	{
		return;
	}
	int st, en;
	if (curlen == 0)
	{
		st = 0;
		en = ll + 2 - (L - curlen);
	}
	else if (curlen == L)
	{
		st = ll;
		en = ll + 1;
	}
	else
	{
		st = 1;
		en = ll + 2 - (L - curlen);
	}
	int pos = line.find('#', srclen);
	if (pos != string::npos && pos < srclen + st)
		return;
	for (int i = st; i < en; ++i)
	{
		if (i > 0 && srclen + i > S)
			return;
		if (i > 0 && src[srclen + i - 1] == '#')
			return;
		if (curlen < L)
		{
			if (srclen + i + lengths[curlen] > S)
				return;
			pos = line.find('.', srclen + i);
			if (pos != string::npos && pos < srclen + i + lengths[curlen])
				continue;
		}
		//curar[curlen] = i
		proc(curlen + 1, ll - i, srclen + i + (curlen < L ? lengths[curlen] : 0));
	}
}

int main()
{
	cout << sizeof(int) << endl;
	int k = 0;
	while (getline(cin, line))
	{
		S = line.find(' ');
		src = line.c_str();
		int pos = S + 1;
		lengths.clear();
		LL = 0;
		while (true)
		{
			int nxt = line.find(',', pos);
			int len;
			if (nxt == string::npos)
				len = line.length() - pos;
			else
				len = nxt - pos;
			int res = stoi(line.substr(pos, len));
			lengths.push_back(res);
			LL += res;
			if (nxt == string::npos)
				break;
			pos = nxt + 1;
		}
		L = lengths.size();
//		for each (int l in lengths)
//			cout << l << ',';
		proc(0, S - LL, 0);
		summ += cntres;
		auto const now = chrono::system_clock::to_time_t(chrono::system_clock::now());
		cout << ctime(&now) << " " << k << ":" << cntres << " " << summ << endl;
		cntres = 0;
		++k;
	}
	cout << "cntres = " << cntres;
}
