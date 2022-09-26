#include "lists.h"

/**
* _realloc - a function to reallocate memory is buffer array gets filled
* Description:
* @bufsize: size of buffer array
* @keep: buffer array
* Return: new buffer array
*/
int *_realloc(int *bufsize, int *keep)
{
	int n;
	int *temp;

	(*bufsize) *= 2;
	temp = malloc(sizeof(int) * (*bufsize));
	if (temp == NULL)
		return (NULL);

	for (n = 0; keep[n]; n++)
		temp[n] = keep[n];

	free(keep);
	keep = temp;
	return (keep);
}

/**
* is_palindrome - a function in C that checks if a
* singly linked list is a palindrome
* Description:
* @head: head node of list
* Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/

int is_palindrome(listint_t **head)
{

	int i, j, len, bufsize = 10;
	int *keep = malloc(sizeof(int) * bufsize);
	listint_t *current;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	current = *head;
	for (i = 0, len = 0; current; i++, len++)
	{
		keep[i] = current->n;
		current = current->next;
		if ((i + 2) > bufsize)
		{
			keep = _realloc(&bufsize, keep);
			if (keep == NULL)
				return (-1);
		}
	}

	for (i = 0, j = len - 1; i < len / 2; i++, j--)
	{
		if (keep[i] != keep[j])
			return (0);
	}
	free(keep);
	return (1);
}
