#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * main - check the code for
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;

    head = NULL;
    add_nodeint_end(&head, 0);
    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 2);
    add_nodeint_end(&head, 7);
    add_nodeint_end(&head, 40);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 402);
    add_nodeint_end(&head, 1024);
    print_listint(head);

    printf("-----------------\n");

    insert_node(&head, 5);
    insert_node(&head, 69);
    insert_node(&head, -8);
    insert_node(&head, 500);
    insert_node(&head, 2040);
    insert_node(&head, 4080);


    print_listint(head);

    free_listint(head);

    return (0);
}
