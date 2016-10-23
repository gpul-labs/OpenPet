<?php

namespace AppBundle\Repository;

use Doctrine\ORM\EntityRepository;

class SpecimenRepository extends EntityRepository
{

    public function filter($request)
    {
        // {{{

        $qb = $this->getEntityManager()->createQueryBuilder();

        $qb->select('s')
            ->from('AppBundle:Specimen', 's')
            ->where('s.deletedAt is null')
            ->orderBy('s.id', 'DESC')
            ;

        return $qb->getQuery()->getResult();

        // }}}
    }

    public function getCountTotal()
    {
        // {{{

        $qb = $this->getEntityManager()->createQueryBuilder();

        $qb->select('count(t.id)')
            ->from('AppBundle:TransportOffer', 't')
            ->where('t.user = :user')
            ->setParameter('user',  $user->getId())
            ->andWhere('t.deletedAt is null')
            ;

        return $qb->getQuery()->getSingleScalarResult();

        // }}}
    }

}
