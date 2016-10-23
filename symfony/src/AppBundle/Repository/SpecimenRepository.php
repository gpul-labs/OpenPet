<?php

namespace AppBundle\Repository;

use Doctrine\ORM\EntityRepository;

class SpecimenRepository extends EntityRepository
{

    public function filter($request, $limit = 2500)
    {
        // {{{

        $qb = $this->getEntityManager()->createQueryBuilder();

        $qb->select('s, o, l, p, r, sp')
            ->from('AppBundle:Specimen', 's')
            ->join('s.race', 'r')
            ->join('r.specie', 'sp')
            ->join('s.origin', 'o')
            ->join('s.location', 'l')
            ->join('l.province', 'p')
            ->where('s.deletedAt is null')
            ->orderBy('s.id', 'DESC')
            ->setMaxResults($limit)
            ;

        if ($request->query->get('specie')) {
            $qb->andWhere('r.specie = :specie');
            $qb->setParameter('specie', $request->query->get('specie'));
        }

        if ($request->query->get('race')) {
            $qb->andWhere('s.race = :race');
            $qb->setParameter('race', $request->query->get('race'));
        }

        if ($request->query->get('location')) {
            $qb->andWhere('s.location = :location');
            $qb->setParameter('location', $request->query->get('location'));
        }

        if ($request->query->get('origin')) {
            $qb->andWhere('s.origin = :origin');
            $qb->setParameter('origin', $request->query->get('origin'));
        }

        if ($request->query->get('from_age')) {
            $minDate = new \DateTime('now');
            $minDate->modify('-' . $request->query->getInt('from_age') . ' years');
            $qb->andWhere('s.birthdate <= :minDate');
            $qb->setParameter('minDate', $minDate->format('Y-m-d'));
        }

        if ($request->query->get('to_age')) {
            $maxDate = new \DateTime('now');
            $maxDate->modify('-' . $request->query->getInt('to_age') . ' years');
            $qb->andWhere('s.birthdate >= :maxDate');
            $qb->setParameter('maxDate', $maxDate->format('Y-m-d'));
        }


        if ($request->query->get('sex')) {
            $qb->andWhere('s.sex = :sex');
            $qb->setParameter('sex', $request->query->get('sex'));
        }

        if ($request->query->get('last')) {
            $qb->setMaxResults($request->query->getInt('last'));
        }

        return $qb->getQuery()->getResult();

        // }}}
    }

    public function getTotalCount()
    {
        // {{{

        $qb = $this->getEntityManager()->createQueryBuilder();

        $qb->select('count(s.id)')
            ->from('AppBundle:Specimen', 's')
            ->where('s.deletedAt is null')
            ;

        return $qb->getQuery()->getSingleScalarResult();

        // }}}
    }

}
