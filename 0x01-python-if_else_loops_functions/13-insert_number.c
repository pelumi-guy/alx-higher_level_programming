#include "lists.h"

/**
* insert_node - a function in C that inserts a number
* into a sorted singly linked list.
* Description:
* @head: head node of sorted linked list
* @n: new data to be added to sorted linked list
* Return: new node
*/

listint_t *insert_node(listint_t **head, int n)
{

	listint_t *new;
	listint_t *current, *prev;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current->n < n && current->next != NULL)
		{
			prev = current;
			current = current->next;
		}

		if (current->next == NULL && current->n < n)
			current->next = new;
		else
		{
			prev->next = new;
			new->next = current;
		}
	}

	return (new);
}
