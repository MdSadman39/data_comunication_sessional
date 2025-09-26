#include <bits/stdc++.h>
using namespace std;

// Calculate number of parity bits required
int calc_parity_bits(int m)
{
    for (int r = 0; r < m; r++)
        if (pow(2, r) >= m + r + 1)
            return r;
    return 0;
}

// Insert parity placeholders at positions 1,2,4,8...
string pos_parity_bits(string data, int r)
{
    int m = data.length();
    string res = "";
    int j = 0, k = 1;

    for (int i = 1; i <= m + r; i++)
    {
        if (i == pow(2, j))
        {
            res += "0"; // parity placeholder
            j++;
        }
        else
        {
            res += data[m - k]; // insert data bits in reverse
            k++;
        }
    }
    reverse(res.begin(), res.end());
    return res;
}

// Calculate parity bits using Even Parity (%2)
string calc_parity(string arr, int r)
{
    int n = arr.length();
    vector<char> res(arr.begin(), arr.end());

    for (int i = 0; i < r; i++)
    {
        int val = 0;

        for (int j = 1; j <= n; j++)
        {
            if (j & (1 << i))
            {
                val += (res[n - j] - '0'); // count number of 1s
            }
        }
        res[n - (1 << i)] = (val % 2 == 0 ? '0' : '1'); // Even parity
    }

    return string(res.begin(), res.end());
}

// Detect error position
int detect_error(string arr, int r)
{
    int n = arr.length();
    int res = 0;

    for (int i = 0; i < r; i++)
    {
        int val = 0;
        for (int j = 1; j <= n; j++)
        {
            if (j & (1 << i))
                val += (arr[n - j] - '0'); // count 1s
        }
        if (val % 2 != 0)
            res += (1 << i); // parity mismatch → error
    }

    return res; // error position in 1-based index
}

int main()
{
    string data;
    cout << "Enter the data bits: ";
    cin >> data;
    int m = data.length();

    // Step 1: Calculate required parity bits
    int r = calc_parity_bits(m);

    // Step 2: Insert parity placeholders
    string arr = pos_parity_bits(data, r);

    // Step 3: Calculate parity values (Even Parity)
    arr = calc_parity(arr, r);
    cout << "Hamming code generated (Even Parity): " << arr << endl;

    // Step 4: Input received code (with/without error)
    string received;
    cout << "Enter received code (with/without error): ";
    cin >> received;

    // Step 5: Detect error
    int error_pos = detect_error(received, r);

    if (error_pos == 0)
    {
        cout << "No error detected in received code." << endl;
    }
    else
    {
        cout << "Error detected at bit position: " << error_pos << endl;

        // Correct the error
        if (received[received.length() - error_pos] == '0')
        {
            received[received.length() - error_pos] = '1';
        }
        else
        {
            received[received.length() - error_pos] = '0';
        }

        cout << "Corrected code: " << received << endl;
    }

    return 0;
}